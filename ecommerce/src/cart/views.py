# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Cart



def cart(request):
    cart_object = Cart.objects.new_or_get(request)
    return render(request, "cart/cart.html", {})
