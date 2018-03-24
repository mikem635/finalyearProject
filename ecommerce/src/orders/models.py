# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cart.models import Cart
from django.db.models.signals import pre_save, post_save
from payment.models import PayeeData


current_id = 0

class Order(models.Model):
    order_id = models.CharField(max_length=120)
    payee_data = models.ForeignKey(PayeeData, null=True, blank=True)
    #billing_addr
    #shipping_addr
    basket = models.ForeignKey(Cart)
    ORDER_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped')
    )
    order_status = models.CharField(max_length=120, default='pending', choices=ORDER_CHOICES)
    total_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)


    def total(self):
        self.total_price = self.basket.total_price
        self.save()

def increase_id():
    global current_id
    current_id = current_id + 1
    return current_id

def reset_id():
    global current_id
    current_id = 0
    return current_id


def pre_save_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = increase_id()
    queryset = Order.objects.filter(basket=instance.basket).exclude(payee_data=instance.payee_data)
    if queryset.exists():
        queryset.update(active=False)

pre_save.connect(pre_save_order_id, sender=Order)

def post_save_total( sender, instance, created, *args, **kwargs):
    if not created:
        basket = instance
        basket_total = basket.total_price
        basket_id = basket.id
        queryset = Order.objects.filter(basket__id=basket_id)
        if queryset.count() == 1:
            order_object = queryset.first()
            order_object.total()

post_save.connect(post_save_total, sender=Cart)

def post_save_total_new_order( sender, instance, created, *args, **kwargs):
    if created:
        instance.total()

post_save.connect(post_save_total_new_order, sender=Order)
