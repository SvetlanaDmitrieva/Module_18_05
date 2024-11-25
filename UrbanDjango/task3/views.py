from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from django.views.generic import TemplateView


def main_page(request):
    title = 'Игровая платформа'
    main_title = 'Главная страница'
    first_ref = 'Главная'
    second_ref = "Магазин"
    third_ref = "Корзина"
    context = {
        'title': title,
        'main_title': main_title,
        'first_ref': first_ref,
        'second_ref': second_ref,
        'third_ref': third_ref
    }
    return render(request, 'platform.html', context)


def game_store_page(request):
    title = 'Лучшие игры для вас'
    text = 'Игры'
    games = {'games': ["Atomic Heart", "Cyberpunk 2077", 'PayDay 2']}
    pay = 'Купить'
    context = {
        'title': title,
        'text': text,
        'games': games,
        'pay': pay
    }
    # mydict = {'games': ["Atomic Heart", "Cyberpunk 2077", 'PayDay 2']}

    return render(request, 'game_store.html', context)


def cart_page(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)
