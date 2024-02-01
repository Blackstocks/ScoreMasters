from django.forms import ModelForm
from django import forms
from scores.models import Score

class usersForm(forms.Form):
    score= forms.NumberInput()
