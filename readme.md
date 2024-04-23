# Django_331 - Учебный проект "Карточки интервального повторения"
## Lesson 48

### Создание проекта Django_331

1. Создали репозиторий
2. Создали проект Django_331
3. Установили зависимости `pip install django==4.2`
4. Сохранили зависимости в файл `requirements.txt` командой `pip freeze > requirements.txt`

Развернуть проект на локальной машине:
 - Склонировать репозиторий командой `git clone
 - Перейти в папку проекта `cd Django_331`
 - Создать виртуальное окружение `python -m venv venv`
 - Активировать виртуальное окружение `source venv/bin/activate`
 - Установить зависимости `pip install -r requirements.txt`

### Создание Django project

1. Создать проект `django-admin startproject anki .`
Этой командой мы создадим проект с именем `anki` в текущей директории.
Точка в конце команды означает, что проект будет создан в текущей директории, 
без создания дополнительной директории с именем проекта.

2. Запуск проекта `python manage.py runserver`
Для запуска проекта, вам нужно использовать терминал, и находясь в директории проекта, на одном уровне с файлом `manage.py`, выполнить команду `python manage.py runserver`
Для остановки сервера используйте комбинацию клавиш `Ctrl+C`

**Команды терминала:**
- `python manage.py runserver` - запуск сервера
- `cd` - смена директории
- `cd..` - переход на уровень выше
- `ls` - просмотр содержимого директории
- `pwd` - показать текущую директорию

3. Создание приложения `python manage.py startapp cards`
После создания приложения, вам нужно зарегистрировать его в файле `settings.py` в разделе `INSTALLED_APPS`
Без этого, полноценно, приложение не будет работать.

### Создали первое представление

```python
from django.http import HttpResponse

def main(request):
    return HttpResponse("Привет, мир!")  # вернет страничку с надписью "Привет, мир!" на русском языке.

```

Чтобы представление заработало, его нужно зарегистрировать в файле `urls.py` конфигурации проекта.

### Создали первый URL

```python
path('', views.main),
```

Теперь, если вы перейдете на главную страницу сайта, то увидите надпись "Привет, мир!"

### Создаем детальное представление карточки по ее ID

Для этого нам нужно создать новый маршрут, с конвертом int, который будет принимать ID карточки.

```python
path('cards/<int:card_id>/', views.card_detail),
```

А так же функцию, которая будет обрабатывать запрос и возвращать страницу с детальной информацией о карточке.

```python
def card_by_id(request, card_id):
    return HttpResponse(f"Карточка с ID {card_id}")
```

### `include` и собственный файл `urls.py` для приложения `cards`

1. Создали еще одно представление `get_all_cards` в файле `views.py`
2. Создали файл `urls.py` в директории приложения `cards`
3. Зарегистрировали новый файл `urls.py` в файле `urls.py` конфигурации проекта с помощью функции `include`
4. Зарегистрировали маршруты без префикса `cards/` в файле `urls.py` приложения `cards`
5. Удалили маршруты `cards/` из файла `urls.py` конфигурации проекта

## Lesson 49

### Настройка конфигурации запуска в PyCharm

1. **Откройте "Edit Configurations"**: В PyCharm перейдите в меню "Run" -> "Edit Configurations" для настройки новой конфигурации запуска.
2. **Добавление новой конфигурации**: Нажмите на плюсик (+) и выберите тип конфигурации для Python.
3. **Заполнение полей конфигурации**:
   - **Название**: Дайте конфигурации понятное имя, чтобы вы могли легко идентифицировать её среди других конфигураций.
   - **Рабочая директория**: Укажите директорию вашего проекта Django. Это папка, где находится файл `manage.py`.
   - **Интерпретатор языка**: Выберите интерпретатор Python для вашего виртуального окружения, если вы его используете, или глобальный интерпретатор, если виртуальное окружение не настроено.
   - **Script path**: Укажите путь к файлу `manage.py` в вашем проекте Django.
   - **Параметры**: Введите `runserver`, чтобы запустить разработческий сервер Django.


### Знакомство с Django Templates (Шаблоны)

1. Создали папку `templates` в директории приложения `cards`
2. Создали файл `catalog.html` в директории `templates/cards`
3. Переписали функцию `get_all_cards` в файле `views.py` так, чтобы она возвращала страницу `catalog.html`
используя функцию `render` из модуля `django.shortcuts`

**commit: `lesson_49: рендер первого шаблона`**

### Работа с шаблоном 
1. Создали словарь с данными в `views.py` и передали его в шаблон
```python
info = {
    "users_count": 100600,
    "cards_count": 100600,
}
```
2. Вставили данные в шаблон `catalog.html` с помощью шаблонного языка Django
3. Подключили BS5 по CDN и стилизовали страницу

**commit: `lesson_49: передал первые данные в шаблон и подключил BS5`**

### Смотрим типы данных внутри шаблона
- Проверили, что можем передать экземпляр класса, и вывести его атрибуты в шаблоне
- Проверили, что можно передать только словарь
- Передали список и вывели его в шаблоне
- Передали список меню и познакомились с конструкцией `{% for item in menu %}`

**commit: `lesson_49: первый цикл в шаблоне`**

### Посмотрели на тег шаблона `if`
- Сделали `<hr>` после каждого элемента списка, кроме последнего

**commit: `lesson_49: первый тег if в шаблоне`**

### Сделали ссылки в меню кликабельными
- Передали в шаблон список словарей, где каждый словарь содержит url и title
- Осталось протестировать шаблонный тег `url`!


**commit: `lesson_49: сделал ссылки в меню кликабельными`**


## Lesson 50

### Как получить успешное прохождение тестов из ДЗ №29
Что в urlpatterns нужно писать, чтобы получлся путь типа '/cards/catalog/1/'? Как пройти тест?

Делаем разбор ДЗ
Определили, что важнейшую роль играет порядок подключения URL-маршрутов в файле `urls.py`,
отрабатывает первый попавшийся маршрут.

Если первый `slug` - то он отработает число.
Если первый `int` - то он НЕ будет отрабатывать строку.

**commit: `hw_29: пофиксили urls.py (порядок имеет значение) и прошли тесты`**

### Изменение структуры `cards/url.py` и `cards/views.py`
Изменил пути и функции для дальнейшего развития проекта.

### Создание базового шаблона `base.html` в корне проекта в папке `templates`
- Создали базовый шаблон `base.html` в папке `templates`
- Указали кастомный, нестандартный путь для Джанго в файле `settings.py` в разделе `TEMPLATES` 
- Прописали там `BASE_DIR / 'templates',`
- Подключили базовый шаблон для теста функции `main` в файле `views.py`

**commit: `lesson_50: создал базовый шаблон base.html`**

### Синтаксис блоков в шаблонах. `{% block %}` и `{% extends %}`

- Описали блок `content` в базовом шаблоне `base.html`
- Создали шаблон `main.html` в папке `templates`, который расширяет базовый шаблон через `{% extends %}`
- Переопределили блок `content` в шаблоне `main.html` через `{% block %}`
- Подключили шаблон `main.html` в функции `main` в файле `views.py`

**commit: `lesson_50: создал шаблон main.html и расширил базовый шаблон`**

### Создание шаблона `nav_menu.html` и подключение его в базовом шаблоне через `{% include %}`
- Создали каталог `includes` в папке `templates` в корне проекта
- Создали шаблон `nav_menu.html` в папке `includes`
- Написли навигационное меню в шаблоне `nav_menu.html`
- Использовали шаблонный тег `{% url %}` который позволяет создавать ссылки на страницы по их именам в файле `urls.py`
- Подключили шаблон `nav_menu.html` в базовом шаблоне `base.html` через `{% include %}`
- Добавили датасет с карточками и меню, чтобы проверить работу шаблона

**commit: `lesson_50: создал шаблон nav_menu.html и подключил его в базовом шаблоне`**

### Работа с шаблонами `about.html`, `catalog.html`, `main.html` а так же модификация `views.py`
- Модифицировали все шаблоны, и сделали так, чтобы они наследовались от базового шаблона
- Модфицировали соответствующие функции в файле `views.py`, чтобы они возвращали нужные шаблоны и принимали данные для меню
- Наладили рендер меню во всех шаблонах, и получили "сквозное" меню на всех страницах

**commit: `lesson_50: модифицировал все шаблоны и функции в views.py - сквозная навигация`**


### Начали работу над каталогом карточек (динамическая вставка данных в шаблон, цикл + `include`)
- Создали `includes` в папке `templates` в приложении `cards`
- Внутри создали шаблон `card_preview.html`
- Шаблон `card_preview.html` принимает на вход словарь с данными о карточке и возвращает карточку,
которая будет вставлена в каталог карточек в шаблоне `catalog.html` в цикле  #TODO: ДОДЕЛАТЬ!)

**commit: `lesson_50: начал работу над каталогом карточек и динамической вставкой данных в шаблон`**

## Lesson 51

### Продолжили работу над каталогом карточек (динамическая вставка данных в шаблон, цикл + `include`)
- Добавили отсутствующий маршрут в файл `urls.py` приложения `cards` (детальное отображение карточки по ID)
- Добавили шаблон `card_detail.html` в папке `templates/cards` 
- Доделали `include` в шаблоне `catalog.html` и вставили в него карточки из словаря
- Обновили функцию `get_detail_card_by_id` - сделали поиск карточки по ID в словаре и возврат шаблона `card_detail.html` ИЛИ 404


**commit: `lesson_51: доделал каталог карточек и детальное отображение карточки по ID`**

### Собственные шаблонные теги через `simple_tag` 
- Создали тег шаблона `markdown_to_html` через `simple_tag` в файле `cards/templatetags/markdown_to_html.py`
- Протестировали его в представлении `card_detail` в шаблоне `card_detail.html`

**commit: `lesson_51: создал собственный тег шаблона markdown_to_html через simple_tag`**
### Фильтры в шаблонах

### Создали папку `static` в приложении `cards` и подключили статику в шаблоне `base.html`
- Создали папку `static` в приложении `cards`
- Создали папку `cards` в папке `static`
- В ней создали папку `css` и файл `main.css`, а так же папку `js` и файл `main.js`
- Создали тестовые стили и скрипт
- Подключили статику в шаблоне `base.html` через тег `{% load static %}` и тег `{% static %}`
- Подключили стили и скрипт в шаблоне `base.html`
- Проверили работу статики на всех страницах


**commit: `lesson_51: подключил статику в шаблоне base.html`**

### Работа с фильтрами в шаблонах
Посмотрели на работу следующих фильтров в шаблоне `card_preview.html`:
- `length`
- `truncatechars`
- `join`

Так же, в шаблон был добавлен цикл для вывода тегов карточки.

**commit: `lesson_51: работа с фильтрами в шаблонах`**

### Сделаем второй вариант шаблонного тега `markdown_to_html` через `inclusion_tag`
- Создали второй вариант шаблонного тега `markdown_to_html` через `inclusion_tag` в файле `cards/templatetags/markdown_to_html.py`
- Создали шаблон `markdown_to_html.html` в папке `templates/cards`
- Протестировали его в представлении `card_detail` в шаблоне `card_detail.html`
- Сравнили работу двух вариантов шаблонного тега

## Lesson 52

### Выполнили служебные миграции
- Выполнили миграции командой `python manage.py migrate`
Это создало служебные таблицы в базе данных, которые используются для работы с пользователями, сессиями, административной панелью и т.д.

- Создали суперпользователя командой `python manage.py createsuperuser`

### Сделали первую модель `Card` и миграции к ней

**commit: `lesson_52: первая модель cards`**

### Знакомство с `Shell Plus` и работа с моделью `Card` в интерактивной оболочке Django
- Установка `Shell Plus` командой `pip install django-extensions`
- Добавление `django_extensions` в `INSTALLED_APPS` в файле `settings.py`
- Запуск `Shell Plus` командой `python manage.py shell_plus` (для отображения SQL запросов в консоли - `python manage.py shell_plus --print-sql`
- Для того, чтобы начать работать с моделью `Card` в интерактивной оболочке Django, нужно выполнить команду `python manage.py shell_plus`


**commit: `lesson_52: установка Shell Plus и подготовка ORM`**

### CRUD Операции с этой моделью
1. Создание записи
card = Card(question='Пайтон или Питон?!', answer='Пайтон')
card.save()

2. Чтение записи
card = Card.objects.get(pk=1)
Мы можем добыть любые данные из записи, просто обратившись к атрибутам модели:
card.question
card.answer
card.upload_date

3. Обновление записи
card = Card.objects.get(pk=1)
card.question = 'Питон или Пайтон?!!'

4. Удаление записи
card = Card.objects.get(pk=1)
card.delete()

5. Как можно откатить миграции?
- Целиком для приложения `cards` командой `python manage.py migrate cards zero`
- Вернуться к конкретной миграции `python manage.py migrate cards 0001_initial`

**commit: `lesson_52: базовые CRUD Операции с моделью Card`**

### Подключение модели `Card` в административной панели
- Создали файл `admin.py` в приложении `cards` (если его нет)
- Зарегистрировали модель `Card` в административной панели
- `settings.py` `LANGUAGE_CODE = 'ru-ru'` - для русского языка в админке

```python
from django.contrib import admin
from .models import Card

# admin.site.register(Card)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
```

- создаем суперпользователя `python manage.py createsuperuser`

**commit: `lesson_52: подключил модель Card в административной панели`**

### Методы объектного менеджера `objects`
- `all()` - возвращает все объекты модели
- `filter()` - возвращает объекты, которые соответствуют условиям фильтрации
- `get()` - возвращает объект, который соответствует условиям фильтрации
- `exclude()` - возвращает объекты, которые НЕ соответствуют условиям фильтрации
- `order_by()` - возвращает объекты, отсортированные по указанному полю
- `first()` - возвращает первый объект из выборки
- `last()` - возвращает последний объект из выборки
- `count()` - возвращает количество объектов в выборке
- `exists()` - возвращает True, если хотя бы один объект соответствует условиям фильтрации
- `delete()` - удаляет объекты, которые соответствуют условиям фильтрации
- `update()` - обновляет объекты, которые соответствуют условиям фильтрации

1. Получили все карточки `Card.objects.all()` - получаем ленивый запрос `LIMIT 21`
НО!
```python
for card in Card.objects.all():
    print(card.question)
```
Этот код не вызовет дополнительных запросов к базе данных, так как `all()` 
возвращает QuerySet, который хранит в себе все объекты модели, которые соответствуют условиям фильтрации.

2. Получили карточку по ID `Card.objects.get(pk=1)`
3. Получили все карточки с вопросом "Пайтон или Питон?!" `Card.objects.filter(question='Пайтон или Питон?')`
4. Получили первую карточку с вопросом "Пайтон или Питон?!" `Card.objects.filter(question='Пайтон или Питон?').first()`
5. Получаем с помощью лукапа `contains` все карточки с вопросом, содержащим слово "или" `Card.objects.filter(question__contains='или')`
6. Считаем карточки с вопросом "Пайтон или Питон?!" `Card.objects.filter(question='Пайтон или Питон?').count()`
7. Считаем все карточки `Card.objects.all().count()`
8. Получаем карточки добавленные во вторник `Card.objects.filter(upload_date__week_day=3)`


**commit: `lesson_52: методы объектного менеджера objects`**

**commit: `hw_30: done`** 
Загрузил решение ДЗ №30

## Lesson 53
https://icons.getbootstrap.com/ - иконки для BS5
Их надо подключить по ссылке в шаблоне `base.html`

### Сделаем чтение из БД в каталоге карточек
- В файле `views.py` в функции `catalog` изменили возврат словаря на возврат списка карточек из БД
- В файле-вставке `include/card_preview.html` изменили вставку данных id карточки на `card.id` (что соответствует полю id в БД)

**commit: `lesson_53: сделал чтение из БД в каталоге карточек`**

### Сделаем детальное отображение карточки из БД по ID
- В файле `views.py` в функции `get_detail_card_by_id` изменили возврат словаря на возврат карточки из БД
- В файлах `card_detail.html`, `card_preview.html` изменили вставку данных просмотров и добавления в избранное на `card.views` и `card.adds` (что соответствует полям views и adds в БД)

**commit: `lesson_53: сделал детальное отображение карточки из БД по ID`**

### Добавили теги в модель `Card`
- Добавили поле `tags` в модель `Card`
- Создали миграцию командой `python manage.py makemigrations`
- Применили миграцию командой `python manage.py migrate`
- Подключили модель `Card` в административной панели через декоратор `@admin.register(Card)`

**commit: `lesson_53: добавил теги в модель Card`**

### Lookups
- Еще раз пробежались по лукапам 

### `get_object_or_404` для детального отображения карточки по ID

**commit: `lesson_53: get_object_or_404 для детального отображения карточки по ID`**

### В общих чертах разобрали `Q` объекты и `F` объекты
- Для `get_detail_card_by_id` сделали увеличение просмотров на + 1 через `F` объект

**commit: `lesson_53: F объект для увеличения просмотров карточки`**

### hw_31:

### Сортировка для каталога 

- **`sort`** - ключ для указания типа сортировки с возможными значениями: `date`, `views`, `adds`.
- **`order`** - опциональный ключ для указания направления сортировки с возможными значениями: `asc`, `desc`. По умолчанию `desc`.
#### Примеры URL-запросов

1. Сортировка по дате добавления в убывающем порядке (по умолчанию): `/cards/catalog/`
2. Сортировка по количеству просмотров в убывающем порядке: `/cards/catalog/?sort=views`
3. Сортировка по количеству добавлений в возрастающем порядке: `/cards/catalog/?sort=adds&order=asc`
4. Сортировка по дате добавления в возрастающем порядке: `/cards/catalog/?sort=date&order=asc`

**commit: `hw_31: сделал сортировку для каталога`**


## Lesson 54
- Разборабли hw_31
- Разборабли hw_32
- Описали модели, чтобы они соответствовали базе данных
- Подключили боевую базу данных SQLite
- Создали служебные таблицы (просто сделали `migrate`)
- Создали файлы миграций
- Применили миграции в фейковом режиме `--fake`
- Проверили что все работает
- Сделали кликабельными теги в каталоге карточек
- Установили `django-debug-toolbar` и настроили его
- Оптимизировали запросы в каталоге
- Подключили кеширование в настройках и кешировали каталог


## Lesson 55
- Типы отношений в базах данных и их реализация в Django
- Создали модель `Tag` и связали ее с моделью `Card` через отношение `ManyToManyField`
- Многие ко многим (ManyToManyField)

### CRUD операции с моделями `Card` и `Tag`
0. Запустим shell plus с print sql командой `python manage.py shell_plus --print-sql`
1. Создадим объекты модели `Tag`:
- `tag1 = Tag.objects.create(name='Python')`
2. Добавим теги к существующим записям. Просто по ID
- `card = Card.objects.get(pk=1)`
- `tag = Tag.objects.get(pk=3)`
- `card.tags.add(tag)`
- `card.tags.all()`
3. Добавим тег по имени "java_script", найдем ID и через ADD добавим к карточке
- `tag = Tag.objects.get(name="java_script")`
4. В один запрос получим карточки по тегу "java_script"
- `Card.objects.filter(tags__name="java_script")`
- cards_by_tag = tag.cards.all()
- Напишем новый запрос, который создаст карточку и добавит к ней теги 

Получаем или создаем теги

Метод `get_or_create` в Django ORM — это удобный способ получить объект из базы данных, 
если он существует, или создать новый, если он не найден. Он возвращает кортеж, содержащий 
объект и булево значение: первый элемент кортежа — это сам объект, второй — флаг, указывающий,
был ли объект создан в результате текущего вызова (True, если объект был создан, и False, 
 
Если объект был получен из базы данных).

```python
tag_names = ["python", "recursion"]
tags = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]  
# Используем индекс [0] чтобы получить объект Tag
```
5. Создаем карточку
new_card = Card(question="Как работает рекурсия в Python?", answer="Рекурсия - это...")
new_card.save()  # Сохраняем карточку в базу данных

6. Добавляем все теги к карточке
for tag in tags:
    new_card.tags.add(tag)
    
7. Получим все карточки, у которых в теге есть "on"
cards = Card.objects.filter(tags__name__icontains="on")

**commit: `lesson_55: многие ко многим (ManyToManyField)`**


### Один ко многим (ForeignKey)

- Создали модель категорий и добавили данные.

### Один ко многим (ForeignKey)

- Создали модель категорий и добавили данные.

1. Получить объект категории ID 1
cat1 = Category.objects.get(pk=1)
2. Получаем все карточки по категории cat1
cat1.cards.all()

3. Нам приходит на вход карточка и категория, которую мы хотим присвоить карточке.
Мы не знаем есть такая категория или нет. Попробуем сделать это через get_or_create

new_card = Card.objects.create(question="Какой-то вопрос", answer="Какой-то ответ")
some_cat = Category.objects.get_or_create(name="Новая категория")[0]

new_card.category = some_cat
new_card.save()

**commit: `lesson_55: один ко многим (ForeignKey)`**

### Агрегирующие функции и аннотации

`Count`, `Sum`, `Avg`, `Max`, `Min`. Метод `values()` 

`count` - количество записей
`sum` - сумма значений
`avg` - среднее значение
`max` - максимальное значение
`min` - минимальное значение

`values()` - возвращает QuerySet, содержащий словари, представляющие объекты модели.

1. Получим категорию pk=1
cat1 = Category.objects.get(pk=1)
2. Посчитаем количество карточек в категории
cat1.cards.count()
3. Получим карточку pk=1
card1 = Card.objects.get(pk=1)
4. Посчитаем количество карточек для каждой категории. Annotate
categories_with_counts = Category.objects.annotate(cards_count=Count('cards')).all()
5. Посчитать сколько тегов у каждой карточки и отсортировать по убыванию
cards_with_tag_counts = Card.objects.annotate(tags_count=Count('tags')).order_by('-tags_count').all()
6. Получим карточку с максимальным количеством тегов aggreate
max_views = Card.objects.aggregate(max_views=Max('views'))
max_tags_card = Card.objects.aggregate(max_tags=Max('tags'))


**commit: `lesson_55: кастомизация админки`**
Двигались по конспекту (до создания собственного фильтра в админке)


## Lesson 56
- Делаем собственный фильтр в админки (Наследование от `SimpleListFilter`)
- Сделали собственный фильтр, который позволяет фильтровать карточки по наличию кода в них `class CardCodeFilter(SimpleListFilter)`

**commit: `lesson_56: Создание своего фильтра SimpleListFilter`**

- Поправили таблицы - к таблице многие-ко-многим добавили поле id - первичный ключ
- Сделали миграции

**commit: `lesson_56: добавил первичный ключ к таблице многие-ко-многим`**

- Установил `django-djazzmin` и настроил его
- `pip install django-djazzmin`
- Добавил `djazzmin` в `INSTALLED_APPS` в файле `settings.py`

**commit: `lesson_56: установил и настроил django-djazzmin`**

- Сделал копию служебного шаблона `change_form.html` и вклинились в `{% block after_field_sets %}`
- Добавил в админке карточек кнопку "Создать карточку с тегами" `{% block object-tools-items %}`

**commit: `lesson_56: кастомизация шаблона change_form.html`**


## Lesson 58

- Разобрали возможность делать dump и load данных в Django
- Команды `dumpdata` и `loaddata`, а так же дополнительные настройки
- Как сделать дамп приложения, как указать отсутпы и кодировку
- Сделали дамп и загрузку данных

**commit: `lesson_58: dump.json`**

### Формы в Django
- Создали форму не связанную с моделью. Форма для добавления карточек
- Создали представление, обрабатывающее метод POST и возвращающее форму
- Создали шаблон для формы
- Протестировали работу формы
- Проверили валидацию формы

**commit: `lesson_58: базовая форма для добавления карточек`**
- Дополнили шаблон с построчным рендером полей ввода
- Добавили категорию как выпадающий список `form.ChoiceField`

**commit: `lesson_58: дополнил шаблон с построчным рендером полей ввода`**
- Передали классы и атрибуты в форму через класс формы
- Поправили шаблон и перешли на BS-5 с адаптивной версткой
- Добавили обработку формы и сохранение данных в представлении

**commit: `lesson_58: BS5 и сохранение данных из формы`**

- Описали собственный класс валидатор `CodeBlockValidator`
- Подключили его в форме
- Протестировали работу валидатора (пока слишком жесткий) - будем выключать и дописывать

**commit: `lesson_58: собственный валидатор CodeBlockValidator`**

## Lesson 59
- Написали форму связанную с моделью
- Обновили представление, чтобы оно работало с формой связанной с моделью
- Код получился вдвое короче
- Добавили валидатор для поля `tags` в форме (отсутствие пробелов)
- Добавили метод очистки тегов в форме
- Проверили работу формы

**commit: `lesson_59: форма добавления карточек связанная с моделью`**

- Базовая форма добавления файла
- Минимальный комплект: класс формы, представление, шаблон
- Получения файла через `chunks()` и сохранение его в файловую систему
- Проблема: перезапись файла при одинаковых именах

**commit: `lesson_59: базовая форма добавления файла`**

## Lesson 60 - Классовые представления

### Разбор ДЗ с поиском в каталоге карточек
- Модифицировали функцию-представление `catalog` в файле `views.py` так, чтобы она принимала GET-параметр `search_query`
- Добавили в шаблон `catalog.html` форму для поиска карточек с GET-параметром `search_query` и радио-кнопками для выбора поля поиска
- Протестировали работу поиска
- Добавили отключение кеширования браузера для страницы каталога, чтобы видеть увеличение просмотров в катаолге

**commit: `lesson_60: разбор ДЗ с поиском в каталоге карточек`**

- Добавили экземпляр пагинатора в представление `catalog` в файле `views.py`
- Добавили работу с пагинатором в шаблоне `catalog.html`

**commit: `lesson_60: добавил пагинацию в каталог карточек`**

### Классовые представления

- Переписали функцию представления add_card на классовое представление с наследованием от `View`

**commit: `lesson_60: переписал функцию представления add_card на классовое представление`**

- Переписали about и главную страницу на классовые представления (наследование от `TemplateView`)
- Создали миксин, который добавляет к контексту меню, подмешали его в один класс


**commit: `lesson_60: переписал about и главную страницу на TemplateView`**

- Добавили в AboutView и IndexView атрибут `extra_context` и добавили в него подсчет
реального количества карточек и пользователей

**commit: `lesson_60: добавил в AboutView и IndexView подсчет реального количества карточек и пользователей`**

## Lesson 61

### ListView
- Переписали представление `catalog` на классовое представление `ListView`
- Добавили жадную загрузку связанных объектов
- Использовали `__iregex` для РАБОЧЕГО регистронезависимого поиска вместо `__icontains` (актуально для SQLite)
- Кешировали каталог силами шаблонизатора
- Использовали `page_obj.paginator.count` для подсчета количества карточек (не иницирует новых запросов к БД)
- Использовали переменные для кеша, которые позволяют кешировать разные варианты страницы (по запросам и сортировкам)`{% cache 90 catalog_content page_obj.number sort order search_query %}`

**commit: `lesson_61: catalog на классовое представление ListView и кеширование`**


### DetailView
- Переписали представление `get_detail_card_by_id` на классовое представление `DetailView`
- Обновили шаблон `card_detail.html` для работы с классовым представлением


**commit: `lesson_61: get_detail_card_by_id на классовое представление DetailView`**


### Кеширование MenuMixin
- Использовали `from django.core.cache import cache` для кеширования меню, так как оно делало с каждой страницы по 2 запроса в БД

**commit: `lesson_61: кеширование меню с помощью cache`**


### CreateView
- Переписали представление добавления карточки на классовое представление `CreateView` - `AddCardCreateView(MenuMixin, CreateView)`

**commit: `lesson_61: добавление карточки на классовое представление CreateView`**

## Lesson 62

### UpdateView и DeleteView
- Добавили представления `UpdateView` и `DeleteView` для редактирования и удаления карточек
- Внесли в форму `CardForm` неудачную правку в инициализатор, попытка изменить теги на строку при открытии формы редактирования
- А так же удачную правку для тегов, чтобы они на самом деле обновлялись (а не только добавлялись)
- Шаблон для 404 ошибки (работает пока только в боевом режиме `DEBUG=False`)

**commit: `lesson_62: UpdateView и DeleteView и 404`**


### Users app
- Создали приложение `users` и подключили его в `INSTALLED_APPS`
- Подготовили маршруты и namespace для приложения `users`

**commit: `lesson_62: users app и подготовка маршрутов`**

- прописали функции-представления для авторизации и выхода из системы
- создали шаблон для входа в систему
- `LoginUserForm` - форма для входа в систему
- Протестировали вход и выход из системы
- Нашли в браузере куки и сессии

**commit: `lesson_62: функции-представления для авторизации и выхода из системы`**

- `redirect_field_name` = 'next' во вьюшке добавления карточек
- Так же, добавили миксин `LoginRequiredMixin` для защиты представлений от неавторизованных пользователей
- В шаблон `login.html` добавили `next` для перехода на страницу, с которой пришел пользователь
`<input type="hidden" name="next" value="{{ request.GET.next }}">`
- Пофиксили редирект при успешной авторизации `return redirect(request.POST.get('next', 'catalog'))`
Это позволяет переходить на страницу, с которой пришел пользователь после авторизации
- Поработали с меню, теперь там отображается имя пользователя и ссылка на выход из системы
- 
**commit: `lesson_62: защита представлений от неавторизованных пользователей и перенаправление`**

## Lesson 63

#BUG: Нашли косяк с кешированием представления по тегам (отображается только кеш первого тега)
#TODO: Добавить оптимизация шаблонов каталога
- base_catalog.html
- include/card_preview.html
- card_detail.html
- catalog.html
- profile_cards.html ?
- cards_by_tag.html (наследуется от base_catalog.html)
- cards_by_category.html (наследуется от base_catalog.html)

### Переписали функцию логина на LoginUser(LoginView)
- Использовали `LoginView` вместо функции `login_user` - это классовое представление для входа в систему
- В нем использовали служебную форму `AuthenticationForm` для входа в систему
- А так же прописали `success_url` для перехода после успешного входа с проверкой на `next`

**commit: `lesson_63: переписал функцию логина на LoginUser(LoginView)`**


- Написали свою форму с наследованием от `AuthenticationForm` и добавили в нее BS5 стили
- Переписали представление выхода из системы на `LogoutUser(LogoutView)`
- Добавили оформления в шаблон `login.html`

**commit: `lesson_63: своя форма входа и выхода из системы`**

- Поэкспериментировали с `LoginRequiredMixin` и порядком его указания в классе представления
- `MenuMixin` никак не влияет на работу `LoginRequiredMixin`
- Прописал в настройках `LOGIN_URL` для того, чтбы не делать это в каждом защищенном представлении
- Убрал `login_url` из 2 защищенных представлений и проверил работу

**commit: `lesson_63: LoginRequiredMixin и LOGIN_URL`**
