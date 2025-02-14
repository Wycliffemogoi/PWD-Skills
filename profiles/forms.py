from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Username",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label="Email",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ProfileForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Name",
    )
    id_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="ID Number",
    )
    ncpwd_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="NCPWD Number",
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Phone Number",
    )
    county = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="County",
    )
    subcounty = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Sub County",
    )
    ward = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Ward",
    )
    skills = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Skills",
    )

    class Meta:
        model = Profile
        fields = ['name', 'id_number', 'ncpwd_number', 'phone_number', 'county', 'subcounty', 'ward', 'level_of_education', 'skills']