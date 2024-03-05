# ./cards/views.py
from django.http import HttpResponse


def main(request):
    return HttpResponse("Привет, мир!")  # вернет страничку с надписью "Привет, мир!" на русском языке.
