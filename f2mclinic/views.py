from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.decorators import EnableUserRequiredMixin
class HomePageView(EnableUserRequiredMixin,LoginRequiredMixin,TemplateView):
	template_name = 'home.html'