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
def pt_event_mngt(request):
    if request.method == 'POST':
        return redirect('pt_event_mngt')
    else:
        context = {
            'event_reg': Registration.objects.filter(participant_fk=Account.objects.get(email=request.user.email))
        }

        print(Registration.objects.filter(id=4))
        return render(request, 'pt_event_mngt.html', context)


@login_required(login_url='login')
def unavailable_page(request):
    return render(request, 'unavailable_page.html')

def pt_event_status_modal(request, pk):
    context = {
        'pk': pk,
        'reg_details': Registration.objects.filter(id=pk),
    }

    return render(request, 'pt_event_status_modal.html', context)

@login_required(login_url='login')
def pt_event_status(request, pk):
    if request.method == 'POST': 
        status = request.POST['status']
        if (status == 'Register'):
            reg_status = Registration.objects.filter(id=pk).update(status_fk=Status.objects.get(name='Registered'))
        elif (status == 'Unregister'):
            reg_status = Registration.objects.filter(id=pk).update(status_fk=Status.objects.get(name='Unregistered'))

        return redirect('pt_event_mngt')
    else:
        return render(request, 'unavailable_page.html')