from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'Home',
        'content':'Магазин гаджетов',
    }
    return render(request, 'main/index.html', context)

def info(request):
    context = {
        'title':'Info',
        'content':'Информация',
        'base_page_text': "Некоторая информация о магазине и товарах",
    }
    return render(request, 'main/info.html', context)
