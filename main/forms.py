from django import forms
from django.forms import ModelForm, fields
from django.forms.widgets import Textarea
from .models import *

# create your forms
class TodoForm(forms.ModelForm):
    titre       = forms.CharField(initial= 'Entrer Titre ')
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    is_doing    = forms.BooleanField(initial = True)
    class Meta: 
        model = Todo
        fields = '__all__'
