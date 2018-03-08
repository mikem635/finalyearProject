# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Event


class EventListView(ListView):
    queryset = Event.objects.all()
    template_name = "events/lists.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventListView, self).get_context_data(*args, **kwargs)
        return context

class EventDetailView(DetailView):
    queryset = Event.objects.all()
    template_name = "events/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
# Create your views here.
