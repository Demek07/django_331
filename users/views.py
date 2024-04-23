from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from .forms import LoginUserForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    redirect_field_name = 'next'

    def get_success_url(self):
        if self.request.POST.get('next', '').strip():
            return self.request.POST.get('next')
        return reverse_lazy('catalog')




def logout_user(request):
    # Вызов функции logout для завершения сессии пользователя
    logout(request)
    # Перенаправление на страницу входа, используя reverse для получения URL по имени
    return redirect(reverse('users:login'))


def signup_user(request):
    return HttpResponse('Регистрация пользователя')
