from urllib.request import HTTPRedirectHandler

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

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
    else:
        return HttpResponseRedirect(reverse('users:login'))


def cart_sub(request, product_slug):
    prod = Product.objects.get(slug=product_slug)

    cart = Cart.objects.filter(user=request.user, product=prod)

    if cart.exists():
        cart = cart.last()
        if cart:
            cart.quantity -= 1
            if cart.quantity <= 0:
                cart.delete()
            else:
                cart.save()
    else:
        Cart.objects.create(user=request.user, product=prod, quantity=1)
    return redirect(request.META.get('HTTP_REFERER'))

def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])


