from django import forms
from .models import *

class Forma(forms.ModelForm):
    class Meta:
        model=Regis
        exclude=[""]