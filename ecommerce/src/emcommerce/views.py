from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .models import UserProfile



from .forms import *

def home_page(request):
    context = {
        "title":"Hello World",
        "content": "Welcome to the home page",

    }

    if request.user.is_authenticated():
        context = {
            "premium_content": "Yeah"
        }
    return render(request, "home.html", context)


def about_page(request):
    context = {
        "title":"About Page",
        "content": "Welcome to the about page"
    }
    return render(request, "home.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"contact page",
        "content": "Welcome to the home contact page",
        "form": contact_form

    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form

    }
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #context['form'] = LoginForm()
            print(request.user.is_authenticated())
            return redirect("/")
        # Redirect to a success page.
        else:
        # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form

    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        profile = new_user.userprofile
        profile.extra_field = form_cleaned_data.get("extra_field")
        profile.save()
    return render(request, "auth/register.html", context)
