from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .models import *


@api_view(['GET'])
def first_page(request):
    response = {}
    all_product = SaleProduct.objects.all()
    all_product = [product.to_json() for product in all_product]
    response ['all_product'] = all_product
    return render(request, 'index.html', response)