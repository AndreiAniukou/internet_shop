from django.db import models
from django.contrib.auth.models import User


class SaleProduct(models.Model):
    name_product = models.CharField(max_length=100, default='Product name', verbose_name='Product name')
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique URL')
    price = models.FloatField()

    def __str__(self):
        return f"{self.name_product} - {self.slug[:10]}"


    def to_json(self):
        return {"product_name":self.name_product,
                "description":self.description,
                "slug":self.slug,
                "price":self.price,
                }