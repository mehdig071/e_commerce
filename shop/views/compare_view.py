from django.shortcuts import render, redirect,get_object_or_404
from shop.services.compare_service import CompareService

def index(request):
    compares = CompareService.get_compared_products_details(request)
    return render(request, 'shop/compare.html', {'compares': compares})


def add_to_compare(request, product_id):
    CompareService.add_product_to_compare(request, product_id)
    return redirect('shop:compare')

def remove_from_compare(request, product_id):
    CompareService.remove_product_from_compare(request, product_id)
    return redirect('shop:compare')