from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    rating = models.IntegerField(default=0)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    image = models.ImageField(null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.name} £{self.price}'