# Generated by Django 4.2 on 2024-04-04 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(db_column='CardID', primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(db_column='Question', max_length=255, verbose_name='Вопрос')),
                ('answer', models.TextField(db_column='Answer', max_length=5000, verbose_name='Ответ')),
                ('upload_date', models.DateTimeField(auto_now_add=True, db_column='UploadDate', verbose_name='Дата загрузки')),
                ('views', models.IntegerField(db_column='Views', default=0, verbose_name='Просмотры')),
                ('adds', models.IntegerField(db_column='Favorites', default=0, verbose_name='В избранном')),
                ('status', models.BooleanField(choices=[(False, 'Не проверено'), (True, 'Проверено')], default=False, verbose_name='Проверено')),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
                'db_table': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='CategoryID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(db_column='TagID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'db_table': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='CardTag',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('card', models.ForeignKey(db_column='CardID', on_delete=django.db.models.deletion.CASCADE, to='cards.card')),
                ('tag', models.ForeignKey(db_column='TagID', on_delete=django.db.models.deletion.CASCADE, to='cards.tag')),
            ],
            options={
                'verbose_name': 'Тег карточки',
                'verbose_name_plural': 'Теги карточек',
                'db_table': 'CardTags',
                'unique_together': {('card', 'tag')},
            },
        ),
        migrations.AddField(
            model_name='card',
            name='category',
            field=models.ForeignKey(db_column='CategoryID', on_delete=django.db.models.deletion.CASCADE, to='cards.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='card',
            name='tags',
            field=models.ManyToManyField(related_name='cards', through='cards.CardTag', to='cards.tag', verbose_name='Теги'),
        ),
    ]
