from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import OrderForm


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


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form': form, 'id': pk}
    return render(request, 'accounts/order_form.html', context)