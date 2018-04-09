from django import forms
from .models import Event
from datetime import datetime

class addToCartForm(forms.Form):
    choices = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Name",
                                                    "id":"form_full_name"}))

class SubmitEventForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Title",
                                                    }))
    slug = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Slug",
                                                    }))
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control",
                                                    "placeholder":"description",
                                                    }))
    location = forms.CharField()
    max_per_person = forms.IntegerField()
    price = forms.DecimalField()
    time_sale_start = forms.DateTimeField(widget=forms.DateTimeInput(),
                                                    initial=datetime.now())
    time_sale_end = forms.DateTimeField(widget=forms.DateTimeInput(),
                                                    initial=datetime.now())
    number_tickets_on_sale = forms.IntegerField()
    SEFS = 'SEFS'
    Medicine = 'Medicine'
    BusinessAndLaw = 'Business And Law'
    ARTS = 'arts'
    ALL = 'All'
    college_choices = (
        (SEFS, 'SEFS'),
        (Medicine, 'Medicine'),
        (BusinessAndLaw, 'Business And Law'),
        (ARTS, 'Arts'),
        (ALL, 'All')
    )
    collegeOnSalleTo = forms.ChoiceField(choices=college_choices)


class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'slug',
            'description',
            'location',
            'max_per_person',
            'time_sale_start',
            'time_sale_end',
            'number_tickets_on_sale',
            'price',
            'collegeOnSalleTo'
        ]
    """
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Title",
                                                    }))
    slug = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Slug",
                                                    }))
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control",
                                                    "placeholder":"description",
                                                    }))
    location = forms.CharField()
    max_per_person = forms.IntegerField()
    price = forms.DecimalField()
    time_sale_start = forms.DateTimeField(widget=forms.DateTimeInput(),
                                                    initial=datetime.now())
    time_sale_end = forms.DateTimeField()
    number_tickets_on_sale = forms.IntegerField()
    SEFS = 'SEFS'
    Medicine = 'Medicine'
    BusinessAndLaw = 'Business And Law'
    ARTS = 'arts'
    ALL = 'All'
    college_choices = (
        (SEFS, 'SEFS'),
        (Medicine, 'Medicine'),
        (BusinessAndLaw, 'Business And Law'),
        (ARTS, 'Arts'),
        (ALL, 'All')
    )
    collegeOnSalleTo = forms.ChoiceField(choices=college_choices)"""
