from django.shortcuts import render, redirect
from .models import *
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

def home(request):
    return render(request, 'home.html')

def event_menu(request):
    if request.method == 'POST': 
        event_name = Event.objects.get(name=request.POST['event'])
        registration = Registration.objects.create(participant_fk=Account.objects.get(email=request.user.email), event_fk=event_name, status_fk=Status.objects.get(name='Registered'))
        registration.save()

        feedback = FeedbackPT.objects.create(participant_fk=Account.objects.get(email=request.user.email), event_fk=event_name, status_fk=Status.objects.get(name='New'))

        # event_PM = list(EventPM.objects.filter(event_fk=event_name))
        # print(event_PM)
        # for PM in event_PM:
        #     print(PM.PM_fk.id)
        #     feedback = Feedback.objects.create(participant_fk=CustomAccount.objects.get(email=request.user.email), event_fk=event_name, reviewer=EventPM.objects.get(PM_fk=PM.PM_fk), status_fk=Status.objects.get(name='New'))
    else:

        context = {
            'event_obj': Event.objects.all()
        }

        return render(request, 'event_menu.html', context)
    
    return render(request, 'event_menu.html')

def event_reg_modal(request, pk):
    context = {
        'pk': pk,
        'event_details': Event.objects.filter(id=pk),
        'pt_details': Account.objects.get(id=pk),
    }

    return render(request, 'event_reg_modal.html', context)

@login_required(login_url='login')
def event_reg(request, pk):
    if request.method == 'POST': 
        event_name = Event.objects.get(name=request.POST['event_name'])
        registration = Registration.objects.create(participant_fk=Account.objects.get(email=request.user.email), event_fk=event_name, status_fk=Status.objects.get(name='Registered'))
        registration.save()
        return redirect('event_menu')
    else:
        return render(request, 'unavailable_page.html')

@login_required(login_url='login')
def unavailable_page(request):
    return render(request, 'unavailable_page.html')