from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,UpdateView
from .forms import ProfileFormSet
# Create your views here.

class ProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name='accounts/profile.html'

    def get_object(self):
        return get_object_or_404(get_user_model(),pk=self.request.user.id)

class EditProfileView(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    fields = []
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return get_object_or_404(get_user_model(),pk=self.request.user.id)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['profile'] = ProfileFormSet(self.request.POST,instance=self.object)
        else:
            data['profile'] = ProfileFormSet(instance=self.object)
        
        return data

    def form_valid(self,form):
        context = self.get_context_data()
        profile = context['profile']
        self.object = form.save()
        if profile.is_valid():
            profile.instance = self.object
            profile.updated_by = self.request.user
            profile.save()
        return super().form_valid(form)