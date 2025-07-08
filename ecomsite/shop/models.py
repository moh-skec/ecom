from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dicount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
