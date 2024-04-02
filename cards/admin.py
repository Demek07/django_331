from django.contrib import admin
from .models import Card
# admin.site.register(Card) - альтернативный способ регистрации модели
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в админке
    list_display = ('question', 'views', 'upload_date')
    # Поля, которые будут ссылками
    list_display_links = ('question', 'upload_date')
    # Поля по которым будет поиск
    search_fields = ('question', 'answer')
    # Поля по которым будет фильтрация
    list_filter = ('category',)

