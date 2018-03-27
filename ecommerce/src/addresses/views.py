# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from payment.models import PayeeData
from .forms import AddressForm
from .models import Address

def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        print(request.POST)
        print(request.POST.get('address_type'))
        instance = form.save(commit=False)
        user = request.user
        payee_data, payee_data_NEW = PayeeData.objects.get_or_create(user= user, email=user.email)
        if payee_data is not None:
            address_type = request.POST.get('address_type', 'shipping')
            instance.payee_data = payee_data
            instance.addr_type = address_type
            instance.save()
            request.session[address_type + "_address_id"] = instance.id
            print(address_type + "_address_id")
        else:
            print("Error here")
            return redirect("checkout")

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("checkout")
    return redirect("checkout")

def checkout_address_use_view(request):
    context = {
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if request.method == "POST":
            print(request.POST)
            address = request.POST.get('shipping_address', None)
            address_type = request.POST.get('address_type', 'shipping')
            user = request.user
            payee_data, payee_data_NEW = PayeeData.objects.get_or_create(user= user, email=user.email)
            if address is not None:
                queryset = Address.objects.filter(payee_data=payee_data, id=address)
                if queryset.exists():
                    request.session[address_type + "_address_id"] = address
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
    return redirect("checkout")
