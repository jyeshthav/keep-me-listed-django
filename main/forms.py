from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Lists, Tasklist
from datetime import datetime

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", )

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class NewTaskForm(forms.ModelForm):

    task_title = forms.CharField(max_length=200)
    task_priority = forms.IntegerField(min_value=1, max_value=10)
    task_due = forms.DateField()

    class Meta:
        model = Tasklist
        fields = ('task_title', 'task_priority', 'task_due', )
    

class NewListForm(forms.ModelForm):
    list_name = forms.CharField(max_length=50)
    list_summary = forms.CharField(max_length=200)
    
    class Meta:
        model = Lists
        fields = ('list_name', 'list_summary',)

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", )