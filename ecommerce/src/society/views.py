# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .models import Society
from .forms import *

User = get_user_model()
def soc_register_page(request):
    if request.user.is_superuser:
        form = RegisterForm(request.POST or None)
        context = {
            "form": form

        }
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            new_user = User.objects.create_user(username, email, password)
            #profile = request.user.userprofile
            #

            society, new_profile = Society.objects.get_or_create(user= new_user)
            society.soc_name = form.cleaned_data.get("society_name")
            society.is_society = True
            society.save()
        return render(request, "society/register_soc.html", context)


def soc_login_page(request):

    form = Soc_LoginForm(request.POST or None)
    context = {
        "form": form

    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/Eventsmanager/")
        # Redirect to a success page.
        else:
        # Return an 'invalid login' error message.
            context = {
                "form": form,
                "error": "Please Try Again"

            }

    return render(request, "society/soc_login.html", context)
