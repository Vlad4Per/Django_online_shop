from django import template

from cart.models import Cart
from orders.models import Order, OrderItem

register = template.Library()

@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)

@register.simple_tag()
def user_orders(request):
    if request.user.is_authenticated:
        return Order.objects.filter(user=request.user)
