from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from student.models import UserProfile
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.template.loader import get_template
from django.utils import timezone

import hashlib
import datetime



from .forms import *

def generate_activation_key(user):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((user + secret_key).encode('utf-8')).hexdigest()


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form

    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            student = get_object_or_404(UserProfile, user=user)
            if student.is_activated:
                login(request, user)
                #context['form'] = LoginForm()
                return redirect("/Events/")
            else:
                context = {
                    "activate": "Your account is inactive. A new link has being sent"

                }
                email = user.email
                student.activation_key = generate_activation_key(username)
                student.key_expires = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
                url = "http://127.0.0.1:8000/activate/"+student.activation_key
                email_context = {
                            'path': url,
                            'email': email
                        }
                send_mail(
                                    "Please actiavte your account",
                                    get_template("registration/emails/verify.txt").render(email_context),
                                    settings.DEFAULT_FROM_EMAIL,
                                    [email],
                                    html_message=get_template("registration/emails/verify.html").render(email_context),
                                    fail_silently=False,
                            )
                student.save()

                return render(request, "auth/login.html", context)


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
        profile, new_profile = UserProfile.objects.get_or_create(user= new_user)
        profile.course = form.cleaned_data.get("course")
        profile.college = form.cleaned_data.get("college")
        profile.year = form.cleaned_data.get("year")
        profile.activation_key = generate_activation_key(username)
        profile.key_expires = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
        url = "http://127.0.0.1:8000/registration/"+profile.activation_key
        email_context = {
                    'path': url,
                    'email': email
                }
        send_mail(
                            "Please actiavte your account",
                            get_template("registration/emails/verify.txt").render(email_context),
                            settings.DEFAULT_FROM_EMAIL,
                            [email],
                            html_message=get_template("registration/emails/verify.html").render(email_context),
                            fail_silently=False,
                    )
        profile.save()
        return render(request, "auth/register.html", context)

    return render(request, "auth/register.html", context)

def activation(request, key):
    activation_expired = False
    already_active = False
    student = get_object_or_404(UserProfile, activation_key=key)
    if student.is_activated == False:
        if timezone.now() > student.key_expires:
            activation_expired = True #Display: offer the user to send a new activation link
            id_user = student.user.id
        else: #Activation successful
            student.is_activated = True
            student.save()

    #If user is already active, simply display error message
    else:
        already_active = True #Display : error message
    return render(request, 'registration/activation.html', locals())



@login_required
def user_account(request):
    context = {
        "user": request.user

    }
    return render(request, "auth/account.html", context)
