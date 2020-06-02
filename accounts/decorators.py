from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
from django.contrib.auth import logout

class AdminUserRequiredMixin(object):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		if not request.user.admin:
			messages.error(request,'Sorry but you are not admin')
			return redirect('home')
		return super(AdminUserRequiredMixin, self).dispatch(request, *args, **kwargs)
	

class EnableUserRequiredMixin(object):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		if not request.user.enable:
			messages.error(request,"Sorry but you don't have the right to access to the application")
			logout(request)
		return super(EnableUserRequiredMixin, self).dispatch(request, *args, **kwargs)