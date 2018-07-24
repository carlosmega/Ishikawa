from django import forms
from django.forms import ModelForm

from .models import Hallazgo
from .models import Causa

from django.forms import inlineformset_factory

class EdithCausa(ModelForm):
    class Meta:
        model = Causa
        fields = ['hallazgo','causa']

    

class HallazgoCreateForm(ModelForm):

    class Meta:
        model = Causa
        fields = ['hallazgo','agrupador','causa']

    def clean(self):
        cleaned_data = super(HallazgoCreateForm, self).clean()
        hallazgo = cleaned_data.get('hallazgo')
        causa = cleaned_data.get('causa')
        if not hallazgo and not causa:
            raise forms.ValidationError('You have to write something!')

class HallazgoForm(ModelForm):
    hallazgo = forms.CharField(widget=forms.TextInput(attrs={'class': 'formulario_hallazgo'}))

    class Meta:
        model = Hallazgo
        fields = '__all__'



