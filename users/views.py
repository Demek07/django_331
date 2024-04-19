from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_user(request):
    return HttpResponse("Вы вошли в систему")  # Временный ответ


def logout_user(request):
    return HttpResponse("Вы вышли из системы")  # Временный ответ