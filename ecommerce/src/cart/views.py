# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Cart
from events.models import Event
from emcommerce.views import login_page



def cart(request):
    if request.user.is_authenticated():
        cart_object, new = Cart.objects.new_or_get(request)
        return render(request, "cart/cart.html", {"cart":cart_object})

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
