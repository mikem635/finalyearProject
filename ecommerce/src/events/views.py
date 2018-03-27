# -*- coding: utf-8 -*-
from __future__ import unicode_literals



import datetime
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.utils import timezone

from .models import Event
from cart.models import Basket
from emcommerce.views import login_page


def EventDetailView(request, slug=None, *args, **kwargs):
    instance = Event.objects.get(slug=slug)
    if instance is None:
        raise Http404("Product doesn't exist")
    n = range(1, instance.max_per_person+1)
    context = {
        'object': instance,
        'range': n
    }
    return render(request, "events/detail.html", context)




def EventListView(request):
    if request.user.is_authenticated():
        profile = request.user.userprofile
        context = {

        }
        print(profile.college)
        if profile.college == "SEFS":
            queryset = Event.objects.filter(collegeOnSalleTo__icontains="sefs", time_sale_start__lte=timezone.now(),
                                time_sale_end__gte=timezone.now(), number_tickets_on_sale__gt=0)
            queryset1 = Event.objects.filter(collegeOnSalleTo__icontains="All", time_sale_start__lte=timezone.now(),
                                time_sale_end__gte=timezone.now(), number_tickets_on_sale__gt=0)
            context = {
                'product' : queryset,
                "course" : profile.college,
                'allSaleProduct' : queryset1

            }
        elif profile.college == "Business And Law":
            queryset = Event.objects.filter(collegeOnSalleTo__icontains="Business And Law", time_sale_start__lte=timezone.now(),
                                time_sale_end__gte=timezone.now(), number_tickets_on_sale__gt=0)
            queryset1 = Event.objects.filter(collegeOnSalleTo__icontains="All", time_sale_start__lte=timezone.now(),
                                time_sale_end__gte=timezone.now(), number_tickets_on_sale__gt=0 )
            context = {
                'product' : queryset,
                "course" : profile.college,
                'allSaleProduct' : queryset1

            }
        elif profile.college == "Medicine":
            queryset = Event.objects.filter(collegeOnSalleTo__icontains="Medicine", time_sale_start__lte=timezone.now(),
                                time_sale_end__gte=timezone.now(), number_tickets_on_sale__gt=0)
            queryset1 = Event.objects.filter(collegeOnSalleTo__icontains="All", time_sale_start__lte=timezone.now(),
                                time_sale_end__gte=timezone.now(), number_tickets_on_sale__gt=0 )
            context = {
                'product' : queryset,
                "course" : profile.college,
                'allSaleProduct' : queryset1

            }
        elif profile.college == "arts":
            queryset = Event.objects.filter(collegeOnSalleTo__icontains="Arts", time_sale_start__lte=timezone.now(),
                                time_sale_end__gte=timezone.now(),number_tickets_on_sale__gt=0)
            queryset1 = Event.objects.filter(collegeOnSalleTo__icontains="All", time_sale_start__lte=timezone.now(),
                                time_sale_end__gte=timezone.now(), number_tickets_on_sale__gt=0)
            context = {
                'product' : queryset,
                "course" : profile.college,
                'allSaleProduct' : queryset1

            }
        return render(request, "events/lists.html", context)
    else:
        return login_page(request)
