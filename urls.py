from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from . import views 

urlpatterns = [
     path('', views.home, name='home'),    
    path('contact/', views.contact, name='contact'),
    path('forum/',views.forum, name='forum'),
    path('about/', views.about, name='about'),
    path('rule/', views.rule, name='rule'),
   
    path('register/', views.register_request, name="register"),
    path("login/", views.loginPage, name="login")
    path('logout/',views.logoutUser, name='logout'),
    path("reset_pw/", auth_views.PasswordResetView.as_view(template_name='html/password_reset.html'),
    name='reset_password' ),
    path("reset_pw_send/", auth_views.PasswordResetDoneView.as_view(template_name='html/password_reset_sent.html'), 
    name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='html/password_reset_form.html'), 
    name='password_reset_confirm' ),
    path("reset_pw_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='html/password_reset_done.html'), 
    name='password_reset_complete' ),

]