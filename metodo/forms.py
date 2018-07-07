from django import forms
from django.forms import ModelForm

from .models import Hallazgo
from .models import Causa

class HallazgoCreateForm(ModelForm):
    class Meta:
        model = Causa
        fields = ['causa']

class HallazgoForm(ModelForm):
    hallazgo = forms.CharField(widget=forms.TextInput(attrs={'class': 'formulario_hallazgo'}))

    class Meta:
        model = Hallazgo
        fields = '__all__'



