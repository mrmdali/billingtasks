from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('my_apps/', views.my_apps, name='my_apps'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('reset_pass/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='reset_password'),

    path('reset_pass_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_send.html'),
         name='password_reset_done'),

    path('reset_pass/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),
         name='password_reset_confirm'),

    path('reset_pass_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
         name='password_reset_complete'),

]