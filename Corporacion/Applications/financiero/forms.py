import datetime
from django.forms import *
from django import forms
from django.contrib.auth import authenticate
from .models import *


class FacturasForm(forms.ModelForm):

    
    class Meta:

        model = FacturasSub
        fields = ['facturas','observacion','consecutivo', 'pagado' ]
        # campos requeridos 
        widgets = {

            "facturas":  HiddenInput(
                attrs={
                    "id": "facturas"
                }
            ),

            "pagado": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "pagado"
                }
            ),
            "observacion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id":"observacion"
                }
            ),
            'consecutivo': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "consecutivo"
                }
            ),
        }
    