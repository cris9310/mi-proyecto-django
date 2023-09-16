import datetime
from django.forms import *
from django import forms
from django.contrib.auth import authenticate
from .models import *


class FacturasForm(forms.ModelForm):
    
    class Meta:

        model = FacturasSub
        fields = ['consecutivo', 'pagado','observacion' ]
        # campos requeridos 
        widgets = {

            "pagado": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "pagado",
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
    
    def __init__(self, *args, **kwargs):
        super(FacturasForm, self).__init__(*args, **kwargs)
        self.fields['observacion'].label = "Observación"
        self.fields['pagado'].label = "Valor a pagar"
