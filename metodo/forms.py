from django import forms
from django.forms import ModelForm

from .models import Hallazgo

class HallazgoForm(ModelForm):
    class Meta:
        model = Hallazgo
        fields = '__all__'