# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Basket, BasketItems
from events.models import Event
from emcommerce.views import login_page
from payment.models import PayeeData
from orders.models import Order
from django.utils import timezone
from addresses.forms import AddressForm
from addresses.models import Address
from decimal import Decimal


def basket(request):
    if request.user.is_authenticated():
        basket_object, new = Basket.objects.new_or_get(request)
        basket_qs = BasketItems.objects.filter(basket=basket_object)
        for items in basket_qs:
            print(items.tickets)
            print(items.count)
        qs = basket_object.tickets.all()
        no_longer_on_sale = " "
        for event in qs:
            #event_object = Event.objects.get(id=event)
            if event.time_sale_end <= timezone.now():
                basket_object.tickets.remove(event)
                no_longer_on_sale += event.title + " "
        context = {
            "basket": basket_object,
            "basket_qs": basket_qs,
            "error": no_longer_on_sale
        }
        request.session['basket_total'] = basket_object.tickets.count()
        return render(request, "basket/basket.html", context)

def basket_update(request):
    if request.user.is_authenticated():
        event = request.POST.get("event_id")
        quantity = request.POST.get("quantity")
        quantity = Decimal(quantity)
        if event is not None:
            event_object = Event.objects.get(id=event)
            price = event_object.price
            basket_object, new = Basket.objects.new_or_get(request)
            basket_items, new_itms = BasketItems.objects.get_or_create(tickets = event_object, basket=basket_object)
            if new_itms:
                print(type(price))
                print(type(quantity))
                print(type(basket_object.total_price))
                basket_object.total_price = Decimal(basket_object.total_price) + (price * quantity)
                basket_object.save()
                basket_items.count = quantity
                basket_items.save()
            else:
                old = basket_items.count
                old_total = basket_object.total_price
                old_total = old_total - (price * old)
                new_total = old_total + (price * quantity)
                basket_object.total_price = new_total
                basket_object.save()
                basket_items.count = quantity
                basket_items.save()

            count = 0
            request.session['basket_total'] = count


    return redirect("Balls")

def remove_item(request):
    if request.user.is_authenticated():
        event = request.POST.get("event_id")
        basket_object, new = Basket.objects.new_or_get(request)
        if event is not None:
            event_object = Event.objects.get(id=event)
            basket_item = BasketItems.objects.get(tickets = event, basket=basket_object)
            quantity = basket_item.count
            price = event_object.price
            total_to_remove = price * quantity
            basket_object.total_price = basket_object.total_price - total_to_remove
            basket_object.save()
            basket_item.delete()
            request.session['basket_total'] = basket_object.tickets.count()
        return redirect("basket")

def checkout(request):
    basket_object, new_basket = Basket.objects.new_or_get(request)
    order_object = None
    address_form = AddressForm()
    billing_id = request.session.get("billing_address_id", None)
    shipping_id = request.session.get("shipping_address_id", None)
    if basket_object.tickets.count() == 0:
        return redirect("basket")
    user = request.user
    payee_data, new_payee = PayeeData.objects.get_or_create(user= user,  email=user.email)
    address_queryset = None
    if payee_data is not None:
        address_queryset = Address.objects.filter(payee_data = payee_data)
        order_object, new = Order.objects.get_or_create(payee_data = payee_data, basket=basket_object, order_status='pending')
        if billing_id:
            order_object.billing_addr = Address.objects.get(id=billing_id)
            #del request.session["billing_id"]

        if shipping_id:
            order_object.shipping_addr = Address.objects.get(id=shipping_id)
            #del request.session["shipping_id"]

        if billing_id or shipping_id:
            order_object.save()

    if request.method == "POST":
        "some check that order is done"
        complete = order_object.done()
        if complete:
            order_object.paid()
            request.session['basket_total'] = 0
            del request.session['basket_id']
            return redirect("Balls")


    context = {
        "object":order_object,
        "payee_date": payee_data,
        "address_form":address_form,
        "address_queryset": address_queryset

    }
    return render(request, "basket/checkout.html", context)
