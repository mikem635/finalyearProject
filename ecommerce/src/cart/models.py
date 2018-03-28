# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import pre_save, m2m_changed

from events.models import Event

from django.db import models
from django.utils import timezone


User = settings.AUTH_USER_MODEL

class BasketManager(models.Manager):
    def new_or_get(self, request):
        basket_id = request.session.get("basket_id", None)
        qs = self.get_queryset().filter(id=basket_id)
        if qs.count() == 1:
            new = False
            basket_object = qs.first()
        else:
            basket_object = self.new_basket(user=request.user)
            new = True
            request.session['basket_id'] = basket_object.id
        return basket_object, new

    def new_basket(self, user=None):
        user_object = None
        if user is not None:
            if user.is_authenticated():
                user_object = user
        return self.model.objects.create(user=user_object)




class Basket(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    tickets = models.ManyToManyField(Event, blank=True, through= 'BasketItems')
    total_price = models.DecimalField(default = 0.0, max_digits = 20, decimal_places = 2)
    objects = BasketManager()

    def __str__(self):
        return str(self.id)

class BasketItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tickets = models.ForeignKey(Event, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    count = models.IntegerField(default = 0)
    complete = models.BooleanField(default=False)




def m2m_changed_basket_rec(sender, instance, action, *args, **kwargs):
    events = instance.tickets.all()
    print(events)
    total = 0
    for event in events:
        total += event.price
    instance.total_price = total
    instance.save()

m2m_changed.connect(m2m_changed_basket_rec, sender=Basket.tickets.through)
