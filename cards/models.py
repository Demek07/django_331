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
"""