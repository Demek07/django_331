# ./cards/views.py
from django.http import HttpResponse
from django.shortcuts import render

info = {
    "users_count": 100600,
    "cards_count": 100600,
    "menu": [
        {"title": "Главная",
         "url": "/",
         "url_name": "index"},
        {"title": "О проекте",
         "url": "/about/",
         "url_name": "about"},
        {"title": "Каталог",
         "url": "/cards/catalog/",
         "url_name": "catalog"},
    ]
}


def main(request):
    return HttpResponse("Привет, мир!")  # вернет страничку с надписью "Привет, мир!" на русском языке.

def card_by_id(request, card_id):
    if card_id > 10:
        return HttpResponse("Такой карточки нет!", status=404)
    return HttpResponse(f"Вы открыли карточку {card_id}")  # вернет страничку с надписью "Вы открыли карточку {card_id}" на русском языке.


def get_all_cards(request):
    """
    Принимает информацию о проекте (словарь info)
    Возвращает шаблон по адресу templates/cards/catalog.html
    :param request:
    :return:
    """
    return render(request, 'cards/catalog.html', context=info)