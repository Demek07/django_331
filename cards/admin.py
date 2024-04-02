from django.contrib import admin
from .models import Card
# admin.site.register(Card) - альтернативный способ регистрации модели
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в админке
    list_display = ('id', 'question', 'category', 'views', 'upload_date', 'status')
    # Поля, которые будут ссылками
    list_display_links = ('id',)
    # Поля по которым будет поиск
    search_fields = ('question', 'answer')
    # Поля по которым будет фильтрация
    list_filter = ('category', 'upload_date', 'status')
    # Ordering - сортировка
    ordering = ('-upload_date',)
    # List_per_page - количество элементов на странице
    list_per_page = 25
    # Поля, которые можно редактировать
    list_editable = ('views', 'question', 'status')
