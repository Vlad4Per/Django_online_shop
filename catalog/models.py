from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="catalog_images")
    price = models.DecimalField(default=0.0, max_digits=9, decimal_places=2)
    discount = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.quantity} штук(-а)'

    def display_id(self):
        return f'{self.id:05}'

    def sell_cost(self):
        if self.discount:
            return round(self.price * (1-self.discount/100),2)
        return self.price

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Products'
        ordering=('id',)
