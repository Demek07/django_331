"""
anki/urls.py
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page
from anki import settings
from cards import views
from django.conf.urls.static import static
from django.conf import settings


# Настраиваем заголовки админ-панели
admin.site.site_header = "Управление моим сайтом" # Текст в шапке
admin.site.site_title = "Административный сайт" # Текст в титле
admin.site.index_title = "Добро пожаловать в панель управления" # Текст на главной странице




urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    # Маршруты для меню
    path('', cache_page(60*15)(views.IndexView.as_view()), name='index'),
    path('about/', cache_page(60*15)(views.AboutView.as_view()), name='about'), 
    # Маршруты подключенные из приложения cards
    path('cards/', include('cards.urls')),
    path('users/', include('users.urls', namespace='users')),
    # Маршруты для авторизации через соцсети
    path('social-auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                      # другие URL-паттерны
                  ] + urlpatterns
    
    # Добавляем обработку медиафайлов
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Определяем кастомный обработчик 404 ошибки
handler404 = views.PageNotFoundView.as_view()