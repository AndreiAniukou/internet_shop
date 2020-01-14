from django.contrib import admin
from .models import SaleProduct


class SaleProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'description']
    prepopulated_fields = {"slug": ["name_product"]}


admin.site.register(SaleProduct, SaleProductAdmin)
