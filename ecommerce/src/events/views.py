# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Event


"""

class EventListView(ListView):
    queryset = Event.objects.all()
    template_name = "events/lists.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventListView, self).get_context_data(*args, **kwargs)
        return context """


def EventDetailView(request, pk=None, *args, **kwargs):
    instance = Event.objects.get_by_id(pk) #id
    if instance is None:
        raise Http404("Product doesn't exist")


    #instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")

    #instance  = Event.objects.filter(id=pk)
    #print(qs)
    """
    if qs.exists() and qs.count() == 1: # len(qs)
        instance = qs.first()
    else:
        raise Http404("Product doesn't exist")"""

    context = {
        'object': instance
    }
    return render(request, "events/detail.html", context)



def EventListView(request):
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
