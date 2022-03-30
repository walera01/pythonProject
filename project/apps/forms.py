from django import forms
from .models import Subs


class Lucky(forms.ModelForm):
    class Meta:
        model = Subs
        exclude = [""]
