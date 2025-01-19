from gc import get_objects

from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from catalog.models import Product
from catalog.utils import q_search

# Create your views here.
def category(request, category_slug=None):
    page = int(request.GET.get('page', 1))
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        products = Product.objects.all()
    elif query:
        products = q_search(query)
    else:
        products = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    if on_sale:
        products = products.filter(discount__gt=0)
    if order_by and order_by != "default":
        products = products.order_by(order_by)

    paginator = Paginator(products, 3)
    cur_page = paginator.page(page)

    context = {
        'title': 'Catalog',
        'products': cur_page,
        'slug_url':category_slug,
    }
    return render(request, 'catalog/category.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product.html', context)
