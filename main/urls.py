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
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    path('homepage', views.homepage, name="homepage"),
    path('register', views.register, name="register"),
    path('logout', views.logout_request, name="logout"),
    path('login', views.login_request, name="login"),
    path('list_form', views.list_form, name="list_form"),
    path('task_form', views.task_form, name="task_form"),
    path('delete_task', views.delete_task, name="delete_task"),
    path('delete_list', views.delete_list, name="delete_list"),
    path('status', views.status, name="status"),
    path('sortby', views.sortby, name="sortby"),
]
