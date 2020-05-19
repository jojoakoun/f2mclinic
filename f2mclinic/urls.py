"""f2mclinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePageView.as_view(),name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('password_reset/done',RedirectView.as_view(pattern_name='accounts:password_reset_done'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',RedirectView.as_view(pattern_name='accounts:password_reset_confirm'),name='password_reset_confirm'),
    path('reset/done',RedirectView.as_view(pattern_name='accounts:password_reset_complete'),name='password_reset_complete'),
]
