from django.urls import path
from . import views

app_name = 'users'  # Пространство имен для приложения

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]