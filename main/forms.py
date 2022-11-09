from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'producer', 'rating', 'duration', 'director']

    def clean_title(self):
        title = self.cleaned_data['title']
        if Film.objects.filter(title=title):
            raise ValidationError('error')
        return title


class UserCreateForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise ValidationError("User with this username already exists!!!")
        return username

    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise ValidationError("Passwords do not match!!1")
        return password1


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Director.objects.filter(name=name):
            raise ValidationError('error')
        return name


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
