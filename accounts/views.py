from django.shortcuts import render,get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,UpdateView,ListView,CreateView,DeleteView,View
from .forms import ProfileFormSet
from django.db import transaction
from .decorators import AdminUserRequiredMixin
# Create your views here.

class ProfileView(LoginRequiredMixin,DetailView):
    template_name='accounts/profile.html'

    def get_object(self):
        return get_object_or_404(get_user_model(),pk=self.request.user.id)

class ShowUserView(LoginRequiredMixin,AdminUserRequiredMixin,DetailView):
    template_name='accounts/show_user.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(get_user_model(),pk=id)

class EditUserView(LoginRequiredMixin,AdminUserRequiredMixin,UpdateView):
    model = get_user_model()
    fields = ['admin']
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts:user_list')

    def get_object(self):
        id = self.kwargs.get('id') 
        return get_object_or_404(get_user_model(),pk=id)

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

class UserListView(LoginRequiredMixin,AdminUserRequiredMixin,ListView):
    template_name = 'accounts/user_list_page.html'
    context_object_name = 'profile_list'

    def get_queryset(self):
        profile_list = Profile.objects.all().order_by('first_name')
        return profile_list

class AddUserView(LoginRequiredMixin,AdminUserRequiredMixin,CreateView):
    model = get_user_model()
    template_name = 'accounts/add_user.html'
    fields = ['email','admin']
    success_url = reverse_lazy('accounts:user_list')

    def get_object(self):
        # return get_object_or_404(get_user_model(),pk=self.request.user.id)
        return get_user_model()
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['profile'] = ProfileFormSet(self.request.POST)
        else:
            data['profile'] = ProfileFormSet()
        return data

    def form_valid(self,form):
        context = self.get_context_data()
        profile = context['profile']
        with transaction.atomic():
            self.object = form.save()
            if profile.is_valid():
                profile.instance = self.object
                profile.created_by = self.request.user
                profile.save()
        return super().form_valid(form)


class DeleteUserView(LoginRequiredMixin,AdminUserRequiredMixin,View):

    def get(self, request,*args, **kwargs):
        id = self.kwargs.get('pk') 
        self.object = get_object_or_404(get_user_model(),pk=id)
        success_url = reverse_lazy('accounts:user_list')
        self.object.delete()
        return HttpResponseRedirect(success_url)

         