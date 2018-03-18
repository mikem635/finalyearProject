# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

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
            queryset = Event.objects.filter(collegeOnSalleTo__icontains="sefs")
            queryset1 = Event.objects.filter(collegeOnSalleTo__icontains="All")
            context = {
                'product' : queryset,
                "course" : profile.college,
                'allSaleProduct' : queryset1

            }
        elif profile.college == "Business And Law":
            queryset = Event.objects.filter(collegeOnSalleTo__icontains="Business And Law")
            queryset1 = Event.objects.filter(collegeOnSalleTo__icontains="All")
            context = {
                'product' : queryset,
                "course" : profile.college,
                'allSaleProduct' : queryset1

            }
        elif profile.college == "Medicine":
            queryset = Event.objects.filter(collegeOnSalleTo__icontains="Medicine")
            queryset1 = Event.objects.filter(collegeOnSalleTo__icontains="All")
            context = {
                'product' : queryset,
                "course" : profile.college,
                'allSaleProduct' : queryset1

            }
        elif profile.college == "arts":
            queryset = Event.objects.filter(collegeOnSalleTo__icontains="Arts")
            queryset1 = Event.objects.filter(collegeOnSalleTo__icontains="All")
            context = {
                'product' : queryset,
                "course" : profile.college,
                'allSaleProduct' : queryset1

            }
        return render(request, "events/lists.html", context)
    else:
        return login_page(request)
