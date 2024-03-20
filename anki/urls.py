"""
anki/urls.py
"""
from django.contrib import admin
from django.urls import path, include
from cards import views

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    # Маршруты для меню
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # Маршруты подключенные из приложения cards
    path('cards/', include('cards.urls')),
]
