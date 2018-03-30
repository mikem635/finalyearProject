# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from events.forms import SubmitEventForm, EditEventForm
from events.models import Event
from cart.models import BasketItems
from society.models import Society
from datetime import datetime
from django.utils import timezone

def submitEvent(request):
    form = SubmitEventForm(request.POST or None)
    context = {
        "form": form
    }
    user = request.user
    society = Society.objects.get(user=user)
    print(society)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        slug = form.cleaned_data.get("slug")
        description = form.cleaned_data.get("description")
        location = form.cleaned_data.get("location")
        max_per_person = form.cleaned_data.get("max_per_person")
        price = form.cleaned_data.get("price")
        time_sale_start = form.cleaned_data.get("time_sale_start")
        time_sale_end = form.cleaned_data.get("time_sale_end")
        number_tickets_on_sale = form.cleaned_data.get("number_tickets_on_sale")
        collegeOnSalleTo = form.cleaned_data.get("collegeOnSalleTo")
        host = society
        event = Event.objects.create(title=title, slug=slug,
                                    description= description, location=location,
                                     max_per_person=max_per_person, price=price,
                                     time_sale_start = time_sale_start, time_sale_end = time_sale_end,
                                     number_tickets_on_sale = number_tickets_on_sale,
                                     collegeOnSalleTo = collegeOnSalleTo,
                                     hosting = host)


    return render(request, "eventmanager/add_event.html", context)


def edit_event(request, slug=None, *args, **kwargs):
    event = Event.objects.get(slug=slug)
    form = EditEventForm(request.POST or None, instance=event)
    context = {
        "form": form
    }
    user = request.user
    society = Society.objects.get(user=user)
    print(society)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        slug = form.cleaned_data.get("slug")
        description = form.cleaned_data.get("description")
        location = form.cleaned_data.get("location")
        max_per_person = form.cleaned_data.get("max_per_person")
        price = form.cleaned_data.get("price")
        time_sale_start = form.cleaned_data.get("time_sale_start")
        time_sale_end = form.cleaned_data.get("time_sale_end")
        number_tickets_on_sale = form.cleaned_data.get("number_tickets_on_sale")
        collegeOnSalleTo = form.cleaned_data.get("collegeOnSalleTo")
        host = society
        event = Event.objects.create(title=title, slug=slug,
                                    description= description, location=location,
                                     max_per_person=max_per_person, price=price,
                                     time_sale_start = time_sale_start, time_sale_end = time_sale_end,
                                     number_tickets_on_sale = number_tickets_on_sale,
                                     collegeOnSalleTo = collegeOnSalleTo,
                                     hosting = host)


    return render(request, "eventmanager/add_event.html", context)


def complete_orders(request, slug=None, *args, **kwargs):
    event = Event.objects.get(slug=slug)
    orders = BasketItems.objects.filter(tickets=event, complete=True)
    for obj in orders:
        print(obj.user.username)
        print(obj.count)
    context = {
        'title': event.title,
        'orders':orders
    }
    return render(request, "eventmanager/orders.html", context)



def event_manager_home(request):
    user = request.user
    society = Society.objects.get(user=user)
    if society.is_society:
        event_queryset_upcoming = Event.objects.filter(hosting = society, time_sale_start__gte=timezone.now())
        event_queryset_active = Event.objects.filter(time_sale_start__lte=timezone.now(),
                            time_sale_end__gte=timezone.now(), number_tickets_on_sale__gt=0)
        event_queryset_past = Event.objects.filter(hosting = society, time_sale_end__lte=timezone.now())
        context = {
            'upcoming' : event_queryset_upcoming,
            'active' : event_queryset_active,
            'past' : event_queryset_past

        }
        return render(request, "eventmanager/lists.html", context)
