from django import forms
from ..models import carrera

class FormCarrera (forms.ModelForm):
    class meta:
        model=carrera
        Fields = ["nombre","descripcion"]
        #Fiels="__al__"