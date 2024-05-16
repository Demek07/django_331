from django.urls import path
from . import views

# Иморт служебных функций для работы с пользователями. django.contrib.auth - это встроенное приложение Django, которое предоставляет функционал для работы с пользователями.
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'users'  # Пространство имен для приложения

urlpatterns = [
    # Вход / Выход / Регистрация
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    # Сообщение об успешной регистрации
    path('register_done/', views.RegisterDoneView.as_view(), name='register_done'),
    # Профиль / Изменение пароля / Мои карточки
    path("profile/", views.ProfileUser.as_view(), name='profile'),
    path("password_change/", views.UserPasswordChange.as_view(), name='password_change'),
    path("passwor_change_done/", views.UserPasswordChangeDone.as_view(), name='password_change_done'),
    path("profile_cards/", views.UserCardsView.as_view(), name='profile_cards'),
    # Профиль / Восстановление пароля
    #########

    # Маршрут для сброса пароля
    path("password-reset/", auth_views.PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ), name="password_reset",
    ),
    
    # Маршрут для подтверждения сброса пароля
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ), name="password_reset_done",
    ),
    
    # Маршрут для ввода нового пароля
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ), name="password_reset_confirm",
    ),
    
    # Маршрут для завершения сброса пароля
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),name="password_reset_complete",
    ),

]