from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tasklist, Lists
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserForm, NewListForm, NewTaskForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request=request,
                template_name='main/index.html',
                # context={'user' : user}
                )

def homepage(request):
    data = {'lists':Lists.objects.filter(list_owner=request.user), 'tasks':Tasklist.objects.filter(task_owner=request.user).order_by('task_due'),
                'user': request.user}
    return render(request = request,
                    template_name = "main/home.html",
                    context=data)

def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as: {username}")
            return redirect('/')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = CustomUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, f"Logged out successfully!")
    return redirect('/')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return render(request = request,
                            template_name = "main/index.html",
                            context={"user":user})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def list_form(request):
    if request.method == 'POST':
        form = NewListForm(request.POST)
        if form.is_valid():
            username = request.user.username
            new_list = form.save(commit=False)
            new_list.list_owner = request.user
            new_list.save()
            messages.success(request, f"List created for: {username}")
            return redirect('/homepage')

        else:
            messages.error(request, "List form entry invalid")
            
    form = NewListForm()
    return render(request = request,
                    template_name = "main/list_form.html",
                    context={"form":form})

def task_form(request):
 
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            username = request.user.username
            new_task = form.save(commit=False)
            new_task.task_list = request.GET.get('task_list')
            new_task.task_owner = request.user
            new_task.save()
            messages.success(request, f"Task created for: {username}")
            return redirect('/homepage')

        else:
            messages.error(request, "List form entry invalid")
    
    form = NewTaskForm()
    return render(request = request,
                    template_name = "main/task_form.html",
                    context={'form': form})

def delete_task(request):

    user = request.user
    tlist = request.GET.get('task_list')
    title = request.GET.get('task_title')
    del_task = get_object_or_404(Tasklist, task_title=title, task_list=tlist, task_owner=user)

    del_task.delete()     
    return redirect('/homepage')

def delete_list(request):
    user = request.user
    tlist = request.GET.get('list_name')
    del_list = get_object_or_404(Lists, list_name=tlist, list_owner=user)
    del_list.delete()     
    return redirect('/homepage')

def status(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        title = request.POST.get('title')
        tlist = request.POST.get('tlist')
        owner = request.POST.get('owner')
        upd_task = Tasklist.objects.get(task_title=title, task_list=tlist, task_owner=request.user, task_status=status)
        if status == '0':
            upd_task.task_status = 1
            upd_task.save()
        elif status == '1':
            upd_task.task_status = 0
            upd_task.save()
        # return render(request = request,
        #             template_name = "main/dummy.html",
        #             context={'user': request.user, 'msg': status})
        return HttpResponse(upd_task.task_status)

def sortby(request):
    if request.method == 'POST':
        data = {Tasklist.objects.filter(task_owner=request.user).order_by('-task_priority')}
        return HttpResponse(data)