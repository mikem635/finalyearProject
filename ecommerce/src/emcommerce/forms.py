from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Student Number",
                                                    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
                                                    "placeholder":"Password",
                                                    }))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Student Number",
                                                    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
                                                    "placeholder":"Password",
                                                    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
                                                    "placeholder":"Confirm Password",
                                                    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control",
                                                    "placeholder":"Your Email",
                                                    }))
    course = forms.CharField(label="Course", max_length=100, widget=forms.TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Your Course",
                                                    }))
    SEFS = 'SEFS'
    Medicine = 'Medicine'
    BusinessAndLaw = 'Business And Law'
    ARTS = 'arts'
    college_choices = (
        (SEFS, 'SEFS'),
        (Medicine, 'Medicine'),
        (BusinessAndLaw, 'Business And Law'),
        (ARTS, 'Arts'),
    )
    college = forms.ChoiceField(choices=college_choices)
    year = forms.CharField(label="Year", max_length=1)


    

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Passwords must match")
        return data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already used")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is already in use")
        return email
