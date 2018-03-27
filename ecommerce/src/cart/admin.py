# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Basket, BasketItems

admin.site.register(Basket)
admin.site.register(BasketItems)
