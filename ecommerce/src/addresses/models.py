# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from payment.models import PayeeData

class Address(models.Model):
        payee_data = models.ForeignKey(PayeeData)
        addr_types = (
            ('billing', 'Billing'),
            ('shipping', 'Shipping'),

        )
        addr_type = models.CharField(max_length=120, choices = addr_types)
        address_line_1 = models.CharField(max_length=120)
        address_line_2 = models.CharField(max_length=120, null=True, blank=True)
        address_line_3 = models.CharField(max_length=120, null=True, blank=True)
        town = models.CharField(max_length=120)
        county = models.CharField(max_length=120)
        eir_code = models.CharField(max_length=120)

        def __str__(self):
            return str(self.payee_data)

        def get_addr(self):
            return "{line1},\n{line2},\n{line3}\n{town},\n{county},\n{eircode}\n".format(
            line1 = self.address_line_1,
            line2 = self.address_line_2 or " ",
            line3 = self.address_line_3 or " ",
            town = self.town,
            county = self.county,
            eircode = self.eir_code
            )
