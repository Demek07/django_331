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
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

import os

info = {
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


class MenuMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = info['menu']
        context['cards_count'] = Card.objects.count()
        context['users_count'] = get_user_model().objects.count()
        return context


class AboutView(MenuMixin, TemplateView):
    """
    Вьюха для статики. Но можно при желании добавить динамический контент
    """
    template_name = 'about.html'
    extra_context = {'title': 'О проекте'} # Обновляется только при загрузке Сервера

    # def get_context_data(self, **kwargs):
    #     # Обновляется при каждом запросе
    #     pass


class IndexView(MenuMixin, TemplateView):
    template_name = 'main.html'

     



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
  

class CatalogView(ListView):
    model = Card  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'cards/catalog.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'cards'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 30  # Количество объектов на странице

    # Метод для модификации начального запроса к БД
    def get_queryset(self):
        # Получение параметров сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'upload_date')
        order = self.request.GET.get('order', 'desc')
        search_query = self.request.GET.get('search_query', '')

        # Определение направления сортировки
        if order == 'asc':
            order_by = sort
        else:
            order_by = f'-{sort}'

        # Фильтрация карточек по поисковому запросу и сортировка
        if search_query:
            queryset = Card.objects.filter(
                Q(question__icontains=search_query) |
                Q(answer__icontains=search_query) |
                Q(tags__name__icontains=search_query)
            ).select_related('category').prefetch_related('tags').order_by(order_by).distinct()
        else:
            queryset = Card.objects.select_related('category').prefetch_related('tags').order_by(order_by)
        return queryset

    # Метод для добавления дополнительного контекста
    def get_context_data(self, **kwargs):
        # Получение существующего контекста из базового класса
        context = super().get_context_data(**kwargs)
        # Добавление дополнительных данных в контекст
        context['sort'] = self.request.GET.get('sort', 'upload_date')
        context['order'] = self.request.GET.get('order', 'desc')
        context['search_query'] = self.request.GET.get('search_query', '')
        # Добавление статических данных в контекст, если это необходимо
        context['menu'] = info['menu'] # Пример добавления статических данных в контекст
        return context


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


class AddCardView(View):
    def get(self, request):
        """
        Обработчик GET запроса формы добавления карточки
        """
        form = CardForm()
        return render(request, 'cards/add_card.html', {'form': form, 'menu': info['menu']})
    
    def post(self, request):
        """
        Обработчик POST запроса формы добавления карточки
        Если форма валидна, сохраняем карточку и делаем редирект на страницу карточки
        Иначе возвращаем форму с ошибками
        """
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            return redirect(card.get_absolute_url())
        return render(request, 'cards/add_card.html', {'form': form, 'menu': info['menu']})