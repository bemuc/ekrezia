from django.forms import ModelForm
from django import forms

from .models import *

class amasakaramentuForm(ModelForm):
    class Meta:
        model = amsakaramentu
        fields = '__all__'
        exclude = ['status','numero']
        widgets = {
            'nomen' : forms.TextInput(attrs={'class':'form-control',}),
            'domicilium' : forms.TextInput(attrs={'class':'form-control',}),
            'pater' : forms.TextInput(attrs={'class':'form-control',}),
            'mater' : forms.TextInput(attrs={'class':'form-control',}),
            'patrinus' : forms.TextInput(attrs={'class':'form-control',}),
            'matrina' : forms.TextInput(attrs={'class':'form-control',}),
            'natus' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'baptizus' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'com_prima' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'com_solen' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'confirmatis' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'matrimonium' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            }