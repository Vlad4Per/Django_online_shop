from django.db import models

from catalog.models import Product
from users.models import User


class OrderItemQueryset(models.QuerySet):
    def total_cost(self):
        return sum(cart.products_price for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=13)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default='В обработке')

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f'Заказ #{self.pk} {self.status} | Получатель:{self.user.first_name} {self.user.last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_item'

    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'Товар - {self.product.name} | Заказ - {self.order.pk}'
