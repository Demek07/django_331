from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest

"""
Бэкенды аутентификации в Django используются для аутентификации пользователей. Они определяют, как пользователи идентифицируются и проверяются.

В Django есть несколько встроенных бэкендов аутентификации, но вы также можете создать свой собственный, как показано в вашем коде.

BaseBackend - это базовый класс для создания бэкендов аутентификации. Он не реализует методы аутентификации, но предоставляет общий интерфейс. Вы можете наследовать от этого класса и реализовать свои собственные методы аутентификации.

get_user_model - это функция, которая возвращает текущую активную модель пользователя. Это полезно, если вы используете пользовательскую модель пользователя вместо стандартной модели пользователя Django. Вы можете использовать эту функцию, чтобы получить доступ к модели пользователя и работать с ней, например, для создания нового пользователя или поиска существующего.

В представленном коде реализован бэкенд аутентификации Django, который позволяет аутентифицировать пользователя по его электронной почте. Однако, в текущей реализации нет возможности аутентифицировать пользователя по его имени пользователя (username).

Метод authenticate пытается найти пользователя по переданному email (который здесь называется username). Если пользователь найден и предоставленный пароль совпадает с паролем пользователя, то метод возвращает этого пользователя. В противном случае, если пользователь не найден или найдено несколько пользователей с таким email, метод возвращает None.
"""

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        
        # Делаем попытку найти пользователя по переданному email
        try:
            user = user_model.objects.get(email=username)
            if user.check_password(password):
                return user
            
        except user_model.DoesNotExist:
            return None
        
        except user_model.MultipleObjectsReturned:
            return None
        
        # def get_user - это метод, который возвращает пользователя по его идентификатору
    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
        
        except user_model.MultipleObjectsReturned:
            return None