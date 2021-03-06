from django import forms

from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'address_line_1',
            'address_line_2',
            'address_line_3',
            'town',
            'county',
            'eir_code'
        ]
