from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def main_page(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'platform.html', context)


def game_store_page(request):
    title = 'Игры'
    games = ["Atomic Heart", "Cyberpunk 2077", 'PayDay 2']
    pay = 'Купить'
    context = {
        'title': title,
        'games': games,
        'pay': pay
    }
    return render(request, 'game_store.html', context)


def cart_page(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)
