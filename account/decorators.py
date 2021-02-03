from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_role):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			if not request.user.is_authenticated:
				return redirect('unavailable_page')
			else:
				flag = False
				for i in range(len(allowed_role)):
					if request.user.role.role_name == allowed_role[i]:
						flag = True

				if (flag):
					return view_func(request, *args, **kwargs)
				else:
					return redirect('unavailable_page')
		return wrapper_func
	return decorator