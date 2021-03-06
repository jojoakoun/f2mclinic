from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views 

app_name = 'accounts'

urlpatterns = [
	path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
	path('logout/',auth_views.LogoutView.as_view(),name='logout'),
	path('password_reset',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
	path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
	path('reset/done',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
	path('profile/',views.ProfileView.as_view(),name='profile'),
	path('profile/edit/',views.EditProfileView.as_view(),name='edit_profile'),
	path('user_list/',views.UserListView.as_view(),name='user_list'),
	path('add_user/',views.AddUserView.as_view(),name='add_user'),
	path('show_user/<int:id>',views.ShowUserView.as_view(),name='show_user'),
	path('edit_user/<int:id>',views.EditUserView.as_view(),name='edit_user'),
	
]