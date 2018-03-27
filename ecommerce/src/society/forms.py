from django import forms
from django.contrib.auth import get_user_model

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Society username",
                                                    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
                                                    "placeholder":"Society Password",
                                                    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
                                                    "placeholder":"Confirm Society Password",
                                                    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control",
                                                    "placeholder":"Society Email",
                                                    }))
    society_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Society Name",
                                                    }))

class Soc_LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Society username",
                                                    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
                                                    "placeholder":"Password",
                                                    }))
