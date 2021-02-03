from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user


@unauthenticated_user
def login(request):
    if request.method == ('POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username=email, password=password)

        if user is not None:

            auth.login(request, user)
            if request.user.is_superuser == True:
                return redirect('home')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Your email/password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')