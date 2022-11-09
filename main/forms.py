from django import forms
from .models import *
from  django.core.exceptions import ValidationError

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'producer', 'rating', 'duration', 'director']

    def clean_title(self):
        title = self.cleaned_data['title']
        if Film.objects.filter(title=title):
            raise ValidationError('error')
        return title

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Director.objects.filter(name=name):
            raise ValidationError('error')
        return name
