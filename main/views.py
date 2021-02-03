from django.shortcuts import render, redirect
from .models import *
from account.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user, allowed_users
from django.utils import timezone
from django.contrib import messages

# Twilio
from twilio.rest import Client

# Email
from raidz_hack2hire.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, BadHeaderError
from django.template import loader
from django.http import HttpResponse

def home(request):

    context = {
        'event_obj': Event.objects.all()
    }
    return render(request, 'home.html', context)

# def event_menu(request):
#     if request.method == 'POST':
#         event_name = Event.objects.get(name=request.POST['event'])
#         # registration = Registration.objects.create(participant_fk=Account.objects.get(email=request.user.email), event_fk=event_name, status_fk=Status.objects.get(name='Registered'))
#         # registration.save()

#         # feedback = FeedbackPT.objects.create(participant_fk=Account.objects.get(email=request.user.email), event_fk=event_name, status_fk=Status.objects.get(name='New'))

#         # event_PM = list(EventPM.objects.filter(event_fk=event_name))
#         # print(event_PM)
#         # for PM in event_PM:
#         #     print(PM.PM_fk.id)
#         #     feedback = Feedback.objects.create(participant_fk=CustomAccount.objects.get(email=request.user.email), event_fk=event_name, reviewer=EventPM.objects.get(PM_fk=PM.PM_fk), status_fk=Status.objects.get(name='New'))
#     else:
#         context = {
#             'event_obj': Event.objects.all()
#         }
#         return render(request, 'event_menu.html', context)

    return render(request, 'event_menu.html')


def event_reg_modal(request, pk):
    context = {
        'pk': pk,
        'event_details': Event.objects.filter(id=pk),
    }

    return render(request, 'event_reg_modal.html', context)


@login_required(login_url='login')
def event_reg(request, pk):
    if request.method == 'POST':

        event_name = Event.objects.get(name=request.POST['event_name'])
        registration = Registration.objects.create(participant_fk=Account.objects.get(
            email=request.user.email), event_fk=event_name, status_fk=Status.objects.get(name='Registered'))
        registration.save()
        feedback = FeedbackPT.objects.create(participant_fk=Account.objects.get(
            email=request.user.email), event_fk=event_name, status_fk=Status.objects.get(name='New'))
        feedback.save()

        event_details = Registration.objects.get(participant_fk=Account.objects.get(
            email=request.user.email), event_fk=event_name, status_fk=Status.objects.get(name='Registered'))

        html_message_template = loader.get_template(
            "sample_email_template.html")
        text_message_template = loader.get_template(
            "sample_email_template.txt")
        body_text = '[Dell Technologies MY] You have successfully registered for ' + str(event_name) + '. Event details are as follows:\n\nStart Datetime: ' + str(
            timezone.localtime(event_details.event_fk.start_datetime)) + '\nEnd Datetime: ' + str(timezone.localtime(event_details.event_fk.end_datetime)) + ''
        message_context = {'name': request.user.full_name,
                           'event_name': event_name,
                           'start_datetime': str(timezone.localtime(event_details.event_fk.start_datetime)),
                           'end_datetime': str(timezone.localtime(event_details.event_fk.end_datetime)),
                           }

        text_message = text_message_template.render(message_context)
        html_message = html_message_template.render(message_context)
        subject = '[Dell Technologies MY]: ' + \
            str(event_name) + ' Registration Successful'
        try:
            # Send email
            # send_mail(subject, text_message, EMAIL_HOST_USER,
            #           [request.user.email], html_message=html_message)

            send_mail(subject, text_message, EMAIL_HOST_USER,
                      ['mdrhmn99@gmail.com'], html_message=html_message)

            account_sid = 'AC221635f6fd44a0ae1e51ff752c25a518'
            auth_token = '43dc4dad503531cadf3072ffccdbf4f0'
            client = Client(account_sid, auth_token)

            # Send SMS
            message = client.messages.create(
                from_='+16319047730',
                body=body_text,
                to='+60148912758'
            )

            # FORMAT:
            # send_mail(subject, message, sender, [recipient])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        messages.success(request, "Event registration successful")

        return redirect('pt_event_mngt')

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

        return render(request, 'pt_event_mngt.html', context)


@login_required(login_url='login')
def unavailable_page(request):
    return render(request, 'unavailable_page.html')

@login_required(login_url='login')
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
            reg_status = Registration.objects.filter(id=pk).update(
                status_fk=Status.objects.get(name='Registered'))
        elif (status == 'Unregister'):
            reg_status = Registration.objects.filter(id=pk).update(
                status_fk=Status.objects.get(name='Unregistered'))

        messages.success(request, "Event registration status change successful")

        return redirect('pt_event_mngt')
    else:
        return render(request, 'unavailable_page.html')

@login_required(login_url='login')
def pt_event_feedback_modal(request, pk):
    event_name = Registration.objects.get(id=pk).event_fk.name

    context = {
        'pk': pk,
        'reg_details': Registration.objects.filter(id=pk),
        'fb_details': FeedbackPT.objects.get(participant_fk__email=request.user.email, event_fk__name=event_name, status_fk=Status.objects.get(name='New')),
    }

    return render(request, 'pt_event_feedback_modal.html', context)


@login_required(login_url='login')
def pt_event_feedback(request, pk):
    if request.method == 'POST':

        suggestions = request.POST['suggestions']
        event_name = request.POST['event_name']

        fb_desc = FeedbackPT.objects.filter(participant_fk__email=request.user.email, event_fk__name=event_name,
                                            status_fk=Status.objects.get(name='New')).update(description=suggestions)

        messages.success(request, "Feedback submission/update successful")

        return redirect('pt_event_mngt')
    else:
        return render(request, 'unavailable_page.html')


@allowed_users(allowed_role=['Committee Lead'])
@login_required(login_url='login')
def cl_event_mngt(request):
    if request.method == 'POST':
        return redirect('cl_event_mngt')
    else:
        context = {
            'event_cat': Category.objects.all(),
            'prog_mgr_list': Account.objects.filter(role__role_name='Program Manager'),
            'cl_list': Account.objects.filter(role__role_name='Committee Lead'),
            'cl_event_list': Event.objects.filter(comm_lead__email=request.user.email)
        }

        return render(request, 'cl_event_mngt.html', context)


@allowed_users(allowed_role=['Program Manager'])
@login_required(login_url='login')
def pm_event_mngt(request):
    if request.method == 'POST':
        return redirect('pm_event_mngt')
    else:
        context = {
            'event_list': Event.objects.all()
        }

        return render(request, 'pm_event_mngt.html', context)


@allowed_users(allowed_role=['Committee Lead'])
@login_required(login_url='login')
def cl_create_event(request):
    if request.method == 'POST':

        # CREATE EVENT
        event_name = request.POST['event_name']
        event_category = Category.objects.get(name=request.POST['category'])
        event_start_datetime = request.POST['start_datetime']
        event_end_datetime = request.POST['end_datetime']
        event_reg_due_datetime = request.POST['reg_due_datetime']
        event_type = request.POST['type']

        if (event_type == 'Virtual'):
            virtual = True
        else:
            virtual = False

        event_desc = request.POST['description']
        event_venue_platform = request.POST['venue_platform']
        prog_mgr = request.POST.getlist('prog_mgr')
        comm_lead = request.POST.getlist('comm_lead')
        img_url = request.POST['img_url']
        speaker = request.POST['speaker']

        create_event = Event.objects.create(name=event_name, category=event_category, description=event_desc, start_datetime=event_start_datetime, end_datetime=event_end_datetime,
                                            reg_due_datetime=event_reg_due_datetime, virtual=virtual, venue_platform=event_venue_platform, img_url=img_url, speaker=speaker, status_fk=Status.objects.get(name='New'))
        set_event_PM = create_event.prog_mgr.set(prog_mgr)
        set_event_CL = create_event.comm_lead.set(comm_lead)

        for PM in prog_mgr:
            create_event_PM = EventPM.objects.create(PM_fk=Account.objects.get(
                id=PM), event_fk=Event.objects.get(name=event_name))

        for CL in comm_lead:
            create_event_CL = EventCL.objects.create(CL_fk=Account.objects.get(
                id=CL), event_fk=Event.objects.get(name=event_name))

        messages.success(request, "Event created successfully")

        # REGISTER EVENT

        registration = Registration.objects.create(participant_fk=Account.objects.get(
            email=request.user.email), event_fk=Event.objects.get(name=event_name), status_fk=Status.objects.get(name='Registered'))
        registration.save()
        feedback = FeedbackPT.objects.create(participant_fk=Account.objects.get(
            email=request.user.email), event_fk=Event.objects.get(name=event_name), status_fk=Status.objects.get(name='New'))
        feedback.save()

        event_details = Registration.objects.get(participant_fk=Account.objects.get(
            email=request.user.email), event_fk=Event.objects.get(name=event_name), status_fk=Status.objects.get(name='Registered'))

        html_message_template = loader.get_template(
            "sample_email_template.html")
        text_message_template = loader.get_template(
            "sample_email_template.txt")
        body_text = '[Dell Technologies MY] You have successfully registered for ' + str(event_name) + '. Event details are as follows:\n\nStart Datetime: ' + str(
            timezone.localtime(event_details.event_fk.start_datetime)) + '\nEnd Datetime: ' + str(timezone.localtime(event_details.event_fk.end_datetime)) + ''
        message_context = {'name': request.user.full_name,
                           'event_name': event_name,
                           'start_datetime': str(timezone.localtime(event_details.event_fk.start_datetime)),
                           'end_datetime': str(timezone.localtime(event_details.event_fk.end_datetime)),
                           }

        text_message = text_message_template.render(message_context)
        html_message = html_message_template.render(message_context)
        subject = '[Dell Technologies MY]: ' + \
            str(event_name) + ' Registration Successful'
        try:
            # Send email
            # send_mail(subject, text_message, EMAIL_HOST_USER,
            #           [request.user.email], html_message=html_message)

            send_mail(subject, text_message, EMAIL_HOST_USER,
                      ['mdrhmn99@gmail.com'], html_message=html_message)

            account_sid = 'AC221635f6fd44a0ae1e51ff752c25a518'
            auth_token = '43dc4dad503531cadf3072ffccdbf4f0'
            client = Client(account_sid, auth_token)

            # Send SMS
            message = client.messages.create(
                from_='+16319047730',
                body=body_text,
                to='+60148912758'
            )

            # FORMAT:
            # send_mail(subject, message, sender, [recipient])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')


        return redirect('cl_event_mngt')
    else:
        return render(request, 'cl_event_mngt.html')


@allowed_users(allowed_role=['Program Manager'])
@login_required(login_url='login')
def pm_event_proposal(request):
    if request.method == 'POST':
        return redirect('pm_event_proposal')
    else:

        context = {
            'event_cat': Category.objects.all(),
            # 'prog_mgr_list': Account.objects.filter(role__role_name='Program Manager'),
            'cl_list': Account.objects.filter(role__role_name='Committee Lead'),
            'proposal_list': EventProposal.objects.filter(prog_mgr=Account.objects.get(email=request.user.email)),
            # 'cl_event_list': Event.objects.filter(comm_lead__email=request.user.email)
        }

        return render(request, 'pm_event_proposal.html', context)


@allowed_users(allowed_role=['Committee Lead'])
@login_required(login_url='login')
def cl_event_proposal(request):
    if request.method == 'POST':
        return redirect('cl_event_proposal')
    else:

        context = {
            'event_cat': Category.objects.all(),
            # 'prog_mgr_list': Account.objects.filter(role__role_name='Program Manager'),
            'cl_list': Account.objects.filter(role__role_name='Committee Lead'),
            'proposal_list': EventProposal.objects.filter(comm_lead=Account.objects.get(email=request.user.email)),
            # 'cl_event_list': Event.objects.filter(comm_lead__email=request.user.email)
        }
        return render(request, 'cl_event_proposal.html', context)


@allowed_users(allowed_role=['Program Manager'])
@login_required(login_url='login')
def pm_propose_event(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        event_category = Category.objects.get(name=request.POST['category'])
        event_type = request.POST['type']
        event_month = request.POST['month']
        event_duration = request.POST['duration']

        if (event_type == 'Virtual'):
            virtual = True
        else:
            virtual = False

        event_desc = request.POST['description']
        # comm_lead = request.POST.getlist('comm_lead')
        comm_lead = request.POST['comm_lead']

        speaker = request.POST['speaker']

        propose_event = EventProposal.objects.create(name=event_name, category=event_category, description=event_desc, month=event_month + "-01", duration=event_duration, speaker=speaker,
                                                     virtual=virtual, prog_mgr=Account.objects.get(email=request.user.email), comm_lead=Account.objects.get(id=comm_lead), status_fk=Status.objects.get(name='New'))
        # set_event_CL = propose_event.comm_lead.set(comm_lead)

        messages.success(request, "Event proposal submission successful")


        return redirect('pm_event_proposal')
    else:
        return render(request, 'pm_event_proposal.html')


@allowed_users(allowed_role=['Program Manager'])
@login_required(login_url='login')
def pm_event_reg(request):
    if request.method == 'POST':

        event_name = request.POST['event_name']
        participants = request.POST.getlist('participants')

        for PT in participants:
            registration = Registration.objects.create(participant_fk=Account.objects.get(
                id=PT), event_fk=Event.objects.get(name=event_name), status_fk=Status.objects.get(name='Registered'))
            registration.save()
            feedback = FeedbackPT.objects.create(participant_fk=Account.objects.get(
                id=PT), event_fk=Event.objects.get(name=event_name), status_fk=Status.objects.get(name='New'))
            feedback.save()

            event_details = Registration.objects.get(participant_fk=Account.objects.get(
                id=PT), event_fk=Event.objects.get(name=event_name), status_fk=Status.objects.get(name='Registered'))
            phone_no = Account.objects.get(id=PT)

            # Your Account Sid and Auth Token from twilio.com/console
            # and set the environment variables. See http://twil.io/secure
            account_sid = 'AC221635f6fd44a0ae1e51ff752c25a518'
            auth_token = '43dc4dad503531cadf3072ffccdbf4f0'
            client = Client(account_sid, auth_token)
            body_text = '[Dell Technologies MY] You have been invited (auto-registered) for ' + str(event_name) + '. Event details are as follows:\n\nStart Datetime: ' + str(
                timezone.localtime(event_details.event_fk.start_datetime)) + '\nEnd Datetime: ' + str(timezone.localtime(event_details.event_fk.end_datetime)) + ''
            # print(body_text)

            # TWILIO SMS
            message = client.messages.create(
                from_='+16319047730',
                body=body_text,
                to=phone_no.phone_number
            )

        messages.success(request, "Event auto-registration/invitation successful")


        return redirect('pm_event_reg')
    else:
        context = {
            'event_cat': Category.objects.all(),
            'pt_list': Account.objects.exclude(role__role_name='Program Manager'),
            'event_list': Event.objects.all()
        }
        return render(request, 'pm_event_reg.html', context)


@allowed_users(allowed_role=['Program Manager'])
@login_required(login_url='login')
def pm_event_feedback(request):
    if request.method == 'POST':
        print()
    else:
        context = {
            'fb_list': FeedbackPT.objects.all()
        }
        return render(request, 'pm_event_feedback.html', context)