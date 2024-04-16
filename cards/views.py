"""
cards/views.py
index - возвращает главную страницу - шаблон /templates/cards/main.html
about - возвращает страницу "О проекте" - шаблон /templates/cards/about.html
catalog - возвращает страницу "Каталог" - шаблон /templates/cards/catalog.html


get_categories - возвращает все категории для представления в каталоге
get_cards_by_category - возвращает карточки по категории для представления в каталоге
get_cards_by_tag - возвращает карточки по тегу для представления в каталоге
get_detail_card_by_id - возвращает детальную информацию по карточке для представления

render(запрос, шаблон, контекст=None)
    Возвращает объект HttpResponse с отрендеренным шаблоном шаблон и контекстом контекст.
    Если контекст не передан, используется пустой словарь.
"""
from re import search
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Card
from django.views.decorators.cache import cache_page

from .templatetags.markdown_to_html import markdown_to_html

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import CardForm, UploadFileForm

import os

info = {
    "users_count": 100500,
    "cards_count": 200600,
    # "menu": ['Главная', 'О проекте', 'Каталог']
    "menu": [
        {"title": "Главная",
         "url": "/",
         "url_name": "index"},
        {"title": "О проекте",
         "url": "/about/",
         "url_name": "about"},
        {"title": "Каталог",
         "url": "/cards/catalog/",
         "url_name": "catalog"},
    ], # Добавим в контекст шаблона информацию о карточках, чтобы все было в одном месте
}


def index(request):
    """Функция для отображения главной страницы
    будет возвращать рендер шаблона root/templates/main.html"""
    return render(request, "main.html", info)


def about(request):
    """Функция для отображения страницы "О проекте"
    будет возвращать рендер шаблона /root/templates/about.html"""
    return render(request, 'about.html', info)


# @cache_page(60 * 15)
def catalog(request):
    """Функция для отображения страницы "Каталог"
    будет возвращать рендер шаблона /templates/cards/catalog.html

    - **`sort`** - ключ для указания типа сортировки с возможными значениями: `date`, `views`, `adds`.
    - **`order`** - опциональный ключ для указания направления сортировки с возможными значениями: `asc`, `desc`. По умолчанию `desc`.

    1. Сортировка по дате добавления в убывающем порядке (по умолчанию): `/cards/catalog/`
    2. Сортировка по количеству просмотров в убывающем порядке: `/cards/catalog/?sort=views`
    3. Сортировка по количеству добавлений в возрастающем порядке: `/cards/catalog/?sort=adds&order=asc`
    4. Сортировка по дате добавления в возрастающем порядке: `/cards/catalog/?sort=date&order=asc`

    """

    # Считываем параметры из GET запроса
    sort = request.GET.get('sort', 'upload_date')  # по умолчанию сортируем по дате загрузки
    order = request.GET.get('order', 'desc')  # по умолчанию используем убывающий порядок
    search_query = request.GET.get('search_query', '')  # поиск по карточкам
    page_number = request.GET.get('page', 1)  # номер страницы

    # Сопоставляем параметр сортировки с полями модели
    valid_sort_fields = {'upload_date', 'views', 'adds'}
    if sort not in valid_sort_fields:
        sort = 'upload_date'

    # Обрабатываем порядок сортировки
    if order == 'asc':
        order_by = sort
    else:
        order_by = f'-{sort}'

    # Если человек ничего не искал
    if not search_query:
        # Получаем карточки из БД в ЖАДНОМ режиме многие ко многим tags
        cards = Card.objects.select_related('category').prefetch_related('tags').order_by(order_by)

    # Если человек что-то искал
    else:
        # Попробуем это сделать без жадной загрузки select_related и prefetch_related
        # cards = Card.objects.filter(question__icontains=search_query).order_by(order_by)
        # Получаем карточки из БД в ЖАДНОМ режиме многие ко многим tags
        # cards = Card.objects.filter(question__icontains=search_query).select_related('category').prefetch_related('tags').order_by(order_by)
        # Q объекты и простая загрузка. Вхождение или в вопрос или в ответ
        # cards = Card.objects.filter(Q(question__icontains=search_query) | Q(answer__icontains=search_query)).order_by(order_by)
        # Q объекты и простая загрузка. Вхождение или в вопрос или в ответ или в теги
        # cards = Card.objects.filter(Q(question__icontains=search_query) | Q(answer__icontains=search_query) | Q(tags__name__icontains=search_query)).order_by(order_by)
        # Это же, с жадной загрузкой
        cards = Card.objects.filter(Q(question__icontains=search_query) | Q(answer__icontains=search_query) | Q(tags__name__icontains=search_query)).select_related('category').prefetch_related('tags').order_by(order_by).distinct()
        
    # Создаем объект пагинатора и передаем ему карточки и количество карточек на странице
    paginator = Paginator(cards, 25)

    # Получаем объект страницы
    page_obj = paginator.get_page(page_number)

    # Подготавливаем контекст и отображаем шаблон
    context = {
        'cards': cards,
        'cards_count': len(cards),
        'menu': info['menu'],
        'page_obj': page_obj,
        "sort": sort, # Передаем, для того чтобы при переходе по страницам сохранялся порядок сортировки
        "order": order, # Аналогично
    }

    response = render(request, 'cards/catalog.html', context)
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # - кэш не используется
    response['Expires'] = '0'  # Перестраховка - устаревание кэша
    return response
  


def get_categories(request):
    """
    Возвращает все категории для представления в каталоге
    """
    # Проверка работы базового шаблона
    return render(request, 'base.html', info)


def get_cards_by_category(request, slug):
    """
    Возвращает карточки по категории для представления в каталоге
    """
    return HttpResponse(f'Cards by category {slug}')


def get_cards_by_tag(request, tag_id):
    """
    Возвращает карточки по тегу для представления в каталоге
    """
    # Добываем карточки из БД по тегу
    cards = Card.objects.filter(tags__id=tag_id)

    # Подготавливаем контекст и отображаем шаблон
    context = {
        'cards': cards,
        'menu': info['menu'],
    }

    return render(request, 'cards/catalog.html', context)


def get_detail_card_by_id(request, card_id):
    """
    Возвращает детальную информацию по карточке для представления
    Использует функцию get_object_or_404 для обработки ошибки 404
    """

    # Добываем карточку из БД через get_object_or_404
    # если карточки с таким id нет, то вернется 404
    card = get_object_or_404(Card, pk=card_id)

    # Обновляем счетчик просмотров через F object
    card.views = F('views') + 1
    card.save()

    card.refresh_from_db()  # Обновляем данные из БД

    # Подготавливаем контекст и отображаем шаблон
    context = {
        'card': card,
        'menu': info['menu'],
    }

    return render(request, 'cards/card_detail.html', context)




def preview_card_ajax(request):
    if request.method == "POST":
        question = request.POST.get('question', '')
        answer = request.POST.get('answer', '')
        category = request.POST.get('category', '')

        # Генерация HTML для предварительного просмотра
        html_content = render_to_string('cards/card_detail.html', {
            'card': {
                'question': question,
                'answer': answer,
                'category': 'Тестовая категория',
                'tags': ['тест', 'тег'],

            }
        }
                                        )

        return JsonResponse({'html': html_content})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            # Редирект на страницу созданной карточки после успешного сохранения
            return redirect(card.get_absolute_url())
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form})


def handle_uploaded_file(f):
    # Создаем путь к файлу в директории uploads, имя файла берем из объекта f
    file_path = f'uploads/{f.name}'

    # Создаем папку uploads, если ее нет
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    
    # Открываем файл для записи в бинарном режиме (wb+)
    with open(file_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return file_path



def add_card_by_file(request):
    if request.method == 'POST':
        
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Записываем файл на диск
            file_path = handle_uploaded_file(request.FILES['file'])
            
            # Редирект на страницу каталога после успешного сохранения
            return redirect('catalog')
    else:
        form = UploadFileForm()
    return render(request, 'cards/add_file_card.html', {'form': form})