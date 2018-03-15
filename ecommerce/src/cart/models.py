# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import pre_save, m2m_changed

from events.models import Event

from django.db import models

User = settings.AUTH_USER_MODEL

class BasketManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("Cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new = False
            cart_object = qs.first()
        else:
            cart_object = self.new_basket(user=request.user)
            new = True
            request.session['Cart_id'] = cart_object.id
        return cart_object, new

    def new_basket(self, user=None):
        user_object = None
        if user is not None:
            if user.is_authenticated():
                user_object = user
        return self.model.objects.create(user=user_object)




class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    tickets = models.ManyToManyField(Event, blank=True)
    total_price = models.DecimalField(default = 0.0, max_digits = 20, decimal_places = 2)

    objects = BasketManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_basket_rec(sender, instance, action, *args, **kwargs):
    events = instance.tickets.all()
    total = 0
    for event in events:
        print(event.price)
        total += event.price
    instance.total_price = total
    instance.save()

m2m_changed.connect(m2m_changed_basket_rec, sender=Cart.tickets.through)
