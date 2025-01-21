from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.db import transaction

from cart.models import Cart
from orders.forms import OrderForm
from orders.models import Order, OrderItem


def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                        )
                        for item in cart_items:
                            product = item.product
                            price = item.product.price
                            quantity = item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {product.name}')
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()
                        cart_items.delete()
                        return redirect('users:profile')
            except Exception as e:
                return redirect('main:index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'title':'Order Form',
    }
    return render(request, 'orders/order.html', context)