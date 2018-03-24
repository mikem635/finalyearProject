# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Cart
from events.models import Event
from emcommerce.views import login_page
from payment.models import PayeeData
from orders.models import Order
from django.utils import timezone
from addresses.forms import AddressForm



def cart(request):
    if request.user.is_authenticated():
        cart_object, new = Cart.objects.new_or_get(request)
        qs = cart_object.tickets.all()
        no_longer_on_sale = " "

        for event in qs:
            #event_object = Event.objects.get(id=event)
            if event.time_sale_end <= timezone.now():
                cart_object.tickets.remove(event)
                no_longer_on_sale += event.title + " "
        print(no_longer_on_sale)
        context = {
            "cart": cart_object,
            "error": no_longer_on_sale
        }
        request.session['cart_total'] = cart_object.tickets.count()
        return render(request, "cart/cart.html", context)

def basket_update(request):
    if request.user.is_authenticated():
        event = request.POST.get("event_id")
        if event is not None:
            event_object = Event.objects.get(id=event)
            cart_object, new = Cart.objects.new_or_get(request)
            cart_object.tickets.add(event_object)
            request.session['cart_total'] = cart_object.tickets.count()


        return redirect("cart")

def remove_item(request):
    if request.user.is_authenticated():
        event = request.POST.get("event_id")

        if event is not None:
            event_object = Event.objects.get(id=event)
            print(event_object)
            cart_object, new = Cart.objects.new_or_get(request)
            if event_object in cart_object.tickets.all():
                cart_object.tickets.remove(event_object)
                request.session['cart_total'] = cart_object.tickets.count()
        return redirect("cart")

def checkout(request):
    basket_object, new_cart = Cart.objects.new_or_get(request)
    order_object = None
    shipping_addr = AddressForm()
    billing_addr = AddressForm()
    if basket_object.tickets.count() == 0:
        return redirect("cart")
    user = request.user
    payee_data, new_payee = PayeeData.objects.get_or_create(user= user, email=user.email)



    order_queryset = Order.objects.filter(basket=basket_object, active=True, payee_data = payee_data)
    if order_queryset.count() == 1:
        order_object = order_queryset.first()
    else:
        order_object = Order.objects.create(payee_data = payee_data, basket=basket_object)


    context = {
        "object":order_object,
        "payee_date": payee_data,
        "shipping_addr" = shipping_addr,
        "billing_addr" = billing_addr

    }
    return render(request, "cart/checkout.html", context)
