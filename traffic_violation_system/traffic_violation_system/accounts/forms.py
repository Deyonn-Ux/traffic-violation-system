from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdateEmailForm(forms.Form):
    email = forms.EmailField(required=True, label='New Email Address')


class UpdateMobileForm(forms.Form):
    mobile_number = forms.CharField(required=True, max_length=20, label='Mobile Number')
