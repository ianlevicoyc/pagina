from django import forms
from .models import ElementoEnUso, ElementoPrestado, Elementos, Alertas
 
class FormElementoEnUso(forms.ModelForm):
    class Meta:
        model = ElementoEnUso
        fields = '__all__'
       
class FormElementoPrestado(forms.ModelForm):
    class Meta:
        model = ElementoPrestado

        fields = '__all__'

class FormElemento(forms.ModelForm):
    class Meta:
        model = Elementos

        fields = '__all__'
    
class FormAlertas(forms.ModelForm):
    class Meta:
        model = Alertas

        fields = '__all__'
       