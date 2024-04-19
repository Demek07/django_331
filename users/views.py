from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginUserForm


def login_user(request):
       if request.method == 'POST':
           form = LoginUserForm(request.POST)
           if form.is_valid():
               username = form.cleaned_data['username']
               password = form.cleaned_data['password']
               user = authenticate(request, username=username, password=password)
               if user is not None:
                   login(request, user)
                   return redirect('catalog')  # Перенаправление на целевую страницу после входа
               else:
                   form.add_error(None, 'Неверное имя пользователя или пароль')
       else:
           form = LoginUserForm()
       return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    # Вызов функции logout для завершения сессии пользователя
    logout(request)
    # Перенаправление на страницу входа, используя reverse для получения URL по имени
    return redirect(reverse('users:login'))

