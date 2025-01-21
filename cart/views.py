from django.shortcuts import render, redirect

from cart.models import Cart
from catalog.models import Product


def cart_add(request, product_slug):
    prod = Product.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=prod)

        if cart.exists():
            cart = cart.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=prod, quantity=1)
    return redirect(request.META.get('HTTP_REFERER'))

def cart_change(request, product_slug):
    ...

def cart_remove(request, product_slug):
    ...

