from django.shortcuts import render, redirect
# from .models import *
from account.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user, allowed_users

# Twilio
# from twilio.rest import Client

# Email
from raidz_hack2hire.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, BadHeaderError
from django.template import loader

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')