"""
Отношения many-to-many.
Делаем модель тегов.
Подключаем её вместо JSON поля в модели Card.

"""
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=75, unique=True)

    class Meta:
        verbose_name = 'Тег'  # имя модели в единственном числе
        verbose_name_plural = 'Теги'  # имя модели во множественном числе

    def __str__(self):
        return f'Тег {self.name}'


class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=5000)
    upload_date = models.DateTimeField(auto_now_add=True, db_column='upload_date')
    views = models.IntegerField(default=0)
    adds = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='cards', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='cards', null=True, blank=True, default=None)

    class Meta:
        db_table = 'Cards'  # имя таблицы в базе данных
        verbose_name = 'Карточка'  # имя модели в единственном числе
        verbose_name_plural = 'Карточки'  # имя модели во множественном числе

    def __str__(self):
        return f'Карточка {self.question} - {self.answer[:50]}'


# Опишем категории для карточек
class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name = 'Категория'  # имя модели в единственном числе
        verbose_name_plural = 'Категории'  # имя модели во множественном числе

    def __str__(self):
        return f'Категория {self.name}'


"""
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
- Добавим тег по имени "java_script", найдем ID и через ADD добавим к карточке
- `tag = Tag.objects.get(name="java_script")`
- В один запрос получим карточки по тегу "java_script"
- `Card.objects.filter(tags__name="java_script")`
- cards_by_tag = tag.cards.all()
- Напишем новый запрос, который создаст карточку и добавит к ней теги 

# Получаем или создаем теги

Метод get_or_create в Django ORM — это удобный способ получить объект из базы данных, 
если он существует, или создать новый, если он не найден. Он возвращает кортеж, содержащий 
объект и булево значение: первый элемент кортежа — это сам объект, второй — флаг, указывающий,
 был ли объект создан в результате текущего вызова (True, если объект был создан, и False, 
 
 если объект был получен из базы данных).

tag_names = ["python", "recursion"]
tags = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]  
# Используем индекс [0] чтобы получить объект Tag

# Создаем карточку
new_card = Card(question="Как работает рекурсия в Python?", answer="Рекурсия - это...")
new_card.save()  # Сохраняем карточку в базу данных

# Добавляем все теги к карточке
for tag in tags:
    new_card.tags.add(tag)
    
# Получим все карточки, у которых в теге есть "on"
cards = Card.objects.filter(tags__name__icontains="on")

"""