from django.shortcuts import render

from catalog.models import Product, Category

# Create your views here.
def category(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'title': 'Catalog',
        'products':product,
        'category':category,
    }
    return render(request,'catalog/category.html', context)

def product(request):
    category = Category.objects.all()
    context = {
        'title': 'Catalog - Product',
        'category':category,
    }
    return render(request,'catalog/product.html', context)