from django.urls import path
from . import views
# cards/urls.py
# будет иметь префикс в urlах /cards/

urlpatterns = [
    # маршрут детального представления карточки в каталоге cards/catalog/1/
    path('catalog/<int:card_id>/', views.get_card_by_id, name='get_card_by_id'),
    # Маршрут категорий cards/catalog/python/
    path('catalog/<slug:slug>/', views.get_category_by_name, name='get_category_by_name'),
    path('', views.get_all_cards, name='all_cards'),
    # маршрут каталога cards/catalog/
    path('catalog/', views.catalog, name='catalog'),
]