from django.urls import path
from . import views
# cards/urls.py
# будет иметь префикс в urlах /cards/

urlpatterns = [
    # Маршрут категорий cards/catalog/python/
    path('catalog/<slug:slug>/', views.card_by_id, name='get_category_by_name'),
    path('', views.get_all_cards, name='all_cards'),
    # маршрут детального представления карточки в каталоге cards/catalog/1/
    path('catalog/<int:card_id>/', views.card_by_id, name='get_card_by_id'),
    # маршрут каталога cards/catalog/
    path('catalog/', views.catalog, name='catalog'),
]