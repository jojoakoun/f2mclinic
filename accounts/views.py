from django.shortcuts import render,get_object_or_404
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
# Create your views here.

class ProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name='accounts/profile.html'

    def get_object(self):
        return get_object_or_404(get_user_model(),pk=self.request.user.id)