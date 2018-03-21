# -*- coding: utf-8 -*-
from __future__ import unicode_literals



import datetime
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.utils import timezone

from .models import Event
from cart.models import Cart
from emcommerce.views import login_page

"""

class EventListView(ListView):
    queryset = Event.objects.all()
    template_name = "events/lists.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventListView, self).get_context_data(*args, **kwargs)
        return context """

class EventDetailView(DetailView):
    querset = Event.objects.all()
    template_name = "events/detail.html"

    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            context = super(EventDetailView, self).get_context_data(*args, **kwargs)
            cart_object, new = Cart.objects.new_or_get(self.request)
            context['cart'] = cart_object
            return context
        else:
            return login_page(request)

    def get_object(self, *args, **kwargs):
        request = self.request
        if request.user.is_authenticated():
            request = self.request
            slug = self.kwargs.get('slug')
            try:
                instance = Event.objects.get(slug=slug) #id
            except Event.DoesNotExist:
                    raise Http404("Not found..")
            if instance is None:
                raise Http404("Product doesn't exist")
            context = {
                'object': instance
            }
            return instance
        else:
            return login_page(request)




def EventListView(request):
    if request.user.is_authenticated():
        profile = request.user.userprofile
        context = {

        }

        if profile.college == "sefs":
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
