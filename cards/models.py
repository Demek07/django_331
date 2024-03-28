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
"""