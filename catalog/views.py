from django.shortcuts import render

from catalog.models import Product, Category

# Create your views here.
def category(request):
    product = Product.objects.all()
    context = {
        'title': 'Catalog',
        'products':product,
        'category':category,
    }
    return render(request,'catalog/category.html', context)

def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product':product,
    }
    return render(request,'catalog/product.html', context)