# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Cart
from events.models import Event



def cart(request):
    cart_object = Cart.objects.new_or_get(request)
    return render(request, "cart/cart.html", {})

def basket_update(request):
    event_object = Event.objects.get(id=1)
    cart_object = Cart.objects.new_or_get(request)
    cart.object.tieckets.add(event_object)

    return redirect()
