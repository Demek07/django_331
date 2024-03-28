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

    class Meta:
        db_table = 'Cards'  # имя таблицы в базе данных
        verbose_name = 'Карточка'  # имя модели в единственном числе
        verbose_name_plural = 'Карточки'  # имя модели во множественном числе

    def __str__(self):
        return f'Карточка {self.question} - {self.answer[:50]}'


"""
## Lesson 55
- Типы отношений в базах данных и их реализация в Django
- Создали модель `Tag` и связали ее с моделью `Card` через отношение `ManyToManyField`
- Многие ко многим (ManyToManyField)

### CRUD операции с моделями `Card` и `Tag`
0. Запустим shell plus командой `python manage.py shell_plus`
"""