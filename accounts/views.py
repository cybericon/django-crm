from django.shortcuts import render
from django.http import HttpResponse

from .models import *


# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    orders_count = orders.count()
    orders_delivered = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="Pending").count()
    context = {
        'customers': customers, 
        'orders' : orders, 
        'orders_count': orders_count, 
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
        }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    return render(request, 'accounts/customer.html', {'customer': customer, 'orders': orders})