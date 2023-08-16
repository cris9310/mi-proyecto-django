import datetime
from django.forms import *
from django import forms
from django.contrib.auth import authenticate
from .models import *


class AgendaRegisterForm(forms.ModelForm):

    
    class Meta:

        model = Evento
        fields = ["title", "descripcion", "start_time", "end_time","hora_inicio", "hora_final", 'color']
        # campos requeridos 
        widgets = {
            
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                     "placeholder": "Ingrese el nombre del evento",
                     "id": "Titulo"
                    }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese la descripción del evento",
                    "id":"Descripcion"
                }
            ),
            "start_time": DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    "type": "date", 
                    "class": "form-control",
                    "id":"FechaInicio"
                },
            ),
            
            "end_time": DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    "type": "date", 
                    "class": "form-control",
                    "id":"FechaFin"
                },
            ),
            "hora_inicio": TimeInput(
                
                attrs={
                    "type": "time",
                    "class": "form-control",
                    "id":"hora_inicio"
                },
            ),
            "hora_final": TimeInput(
                
                attrs={
                    "type": "time",
                    "class": "form-control",
                    "id":"horafinal"
                },
            ),
            "color": forms.TextInput(
                attrs={
                    "type": "color",
                    "class": "form-control",
                    "id":"color"
                }
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super(AgendaRegisterForm, self).__init__(*args, **kwargs)
        # Al iniciar el form la data de estos campos tendrá este formato
        self.fields["start_time"].input_formats = ('%Y-%m-%d',)
        self.fields["end_time"].input_formats = ('%Y-%m-%d',)

        
