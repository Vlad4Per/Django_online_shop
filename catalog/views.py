from gc import get_objects

from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from catalog.models import Product


# Create your views here.
def category(request, category_slug):
    page = int(request.GET.get('page', 1))
    if category_slug == 'all':
        products = Product.objects.all()
    else:
        products = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    paginator = Paginator(products, 1)
    cur_page = paginator.page(page)

    context = {
        'title': 'Catalog',
        'products': cur_page,
    }
    return render(request, 'catalog/category.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product.html', context)
