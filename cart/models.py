from django.db import models
from django.db.models import Sum

from catalog.models import Product
from users.models import User

class CartQueryset(models.QuerySet):
    def total_carts_cost(self):
        return sum(cart.total_cost() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=40, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart'
        ordering = ['-created_timestamp']

    objects = CartQueryset.as_manager()
    def total_cost(self):
        return round(self.quantity * self.product.sell_cost(), 2)

    def __str__(self):
        return f'{self.user.username} - Товар: {self.product.name} в количестве {self.quantity}'