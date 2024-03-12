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