from gc import get_objects

from django.shortcuts import render, get_object_or_404

from catalog.models import Product

# Create your views here.
def category(request, category_slug):
    if category_slug=='all':
        product = Product.objects.all()
    else:
        product = get_object_or_404(Product.objects.filter(category__slug=category_slug))
    context = {
        'title': 'Catalog',
        'products':product,
    }
    return render(request,'catalog/category.html', context)

def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product':product,
    }
    return render(request,'catalog/product.html', context)