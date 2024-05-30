from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from your_app_name.models import Card  # Замените 'your_app_name' на имя вашего приложения

class Command(BaseCommand):
    help = 'Создание группы Модераторы и назначение права change_card'

    def handle(self, *args, **kwargs):
        # Создаем или получаем группу "Модераторы"
        moderators_group, created = Group.objects.get_or_create(name='Модераторы')
        
        # Получаем контентный тип для модели Card
        content_type = ContentType.objects.get_for_model(Card)
        
        # Получаем разрешение change_card
        change_card_permission = Permission.objects.get(codename='change_card', content_type=content_type)
        
        # Добавляем разрешение группе "Модераторы"
        moderators_group.permissions.add(change_card_permission)
        
        if created:
            self.stdout.write(self.style.SUCCESS("Группа 'Модераторы' создана и права назначены!"))
        else:
            self.stdout.write(self.style.SUCCESS("Группа 'Модераторы' уже существует и права обновлены!"))