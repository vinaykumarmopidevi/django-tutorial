from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')