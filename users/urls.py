from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password_form.html'),
    name='password_change'),
    path('password_change_complete/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'),
    name='password_change_done'),
]