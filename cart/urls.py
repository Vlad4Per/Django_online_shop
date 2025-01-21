from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('cart_add/<slug:product_slug>', views.cart_add, name='cart_add'),
    path('cart_sub/<slug:product_slug>', views.cart_sub, name='cart_sub'),
    path('cart_remove/<int:cart_id>', views.cart_remove, name='cart_remove'),
]