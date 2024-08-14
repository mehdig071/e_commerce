from django.shortcuts import get_object_or_404, render, redirect
from shop.models.Order import Order

def index(request):
    user = request.user 
    if not user.is_authenticated:
        return redirect('shop:home')
    
    orders = Order.objects.prefetch_related('order_details').filter(author=user, is_paid=True)
  
    return render(request, 'dashboard/index.html', {
        'page': 'orders', 
        'orders': orders
        })