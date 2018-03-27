# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cart.models import Basket
from django.db.models.signals import pre_save, post_save
from payment.models import PayeeData
from addresses.models import Address


current_id = 0

class Order(models.Model):
    order_id = models.CharField(max_length=120)
    payee_data = models.ForeignKey(PayeeData, null=True, blank=True)
    billing_addr = models.ForeignKey(Address, related_name= "billing_addr",null=True, blank=True)
    shipping_addr = models.ForeignKey(Address,related_name= "shipping_addr", null=True, blank=True)
    basket = models.ForeignKey(Basket)
    ORDER_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('complete', 'Complete')
    )
    order_status = models.CharField(max_length=120, default='pending', choices=ORDER_CHOICES)
    total_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)


    def total(self):
        self.total_price = self.basket.total_price
        self.save()

    def done(self):
        payee_data = self.payee_data
        billing_addr = self.billing_addr
        shipping_addr = self.shipping_addr
        total_price = self.total_price
        if payee_data and billing_addr and shipping_addr and total_price:
            return True
        return False

    def paid(self):
        if self.done():
            self.order_status = 'complete'
            self.save()
        return self.order_status


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

post_save.connect(post_save_total, sender=Basket)

def post_save_total_new_order( sender, instance, created, *args, **kwargs):
    if created:
        instance.total()

post_save.connect(post_save_total_new_order, sender=Order)
