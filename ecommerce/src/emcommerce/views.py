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
    #profile = request.user.userprofile
    if request.user.is_authenticated():
        context = {
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
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("/Events/")
        # Redirect to a success page.
        else:
        # Return an 'invalid login' error message.
            context = {
                "form": form,
                "error": "Please Try Again"

            }

    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form

    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        #profile = request.user.userprofile
        #
        """try:
            profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile(user=request.user)"""
        profile, new_profile = UserProfile.objects.get_or_create(user= new_user)
        profile.course = form.cleaned_data.get("course")
        profile.college = form.cleaned_data.get("college")
        profile.year = form.cleaned_data.get("year")
        profile.save()
    return render(request, "auth/register.html", context)
