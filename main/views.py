from django.shortcuts import render
from catalog.models import Category

def index(request):
    category = Category.objects.all()
    context = {
        'title':'Home',
        'content':'Магазин гаджетов',
        'category':category,
    }
    return render(request, 'main/index.html', context)

def info(request):
    category = Category.objects.all()
    context = {
        'title':'Info',
        'content':'Информация',
        'base_page_text': "Некоторая информация о магазине и товарах",
        'category': category,
    }
    return render(request, 'main/info.html', context)
