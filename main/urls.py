"""mysite URL Configuration

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
from django.urls import path, include
from . import views
# from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    path('homepage', views.homepage, name="homepage"),
    path('register', views.register, name="register"),
    path('edit', views.edit, name="edit"),
    path('change_pass', views.change_pass, name="change_pass"),
    path('logout', views.logout_request, name="logout"),
    path('login', views.login_request, name="login"),
    path('list_form', views.list_form, name="list_form"),
    path('task_form', views.task_form, name="task_form"),
    path('delete_task', views.delete_task, name="delete_task"),
    path('delete_list', views.delete_list, name="delete_list"),
    path('status', views.status, name="status"),
    path('sortby', views.sortby, name="sortby"),

    # path('password-reset/', auth_views.PasswordResetView.as_view(
    #                         template_name='main/registration/password_reset_form.html',
    #                         subject_template_name='main/registration/password_reset_subject.txt',
    #                         email_template_name='main/registration/password_reset_email.html',
    #                         success_url='/password-reset/done'
    # ), name="password_reset"),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
    #                         template_name='main/registration/password_reset_done.html'
    # ), name="password_reset_done"),
    # path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #                         template_name='main/registration/password_reset_confirm.html',
    #                         success_url='/password-reset-complete'
    # ), name="password_reset_confirm"),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    #                         template_name='main/registration/password_reset_complete.html'
    # ), name="password_reset_complete"),
]
