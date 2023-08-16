from django.forms import *
from django import forms
from .models import *
from datetime import date
from .choices import ROLES, PROGRAMAS_TIPOS
import pandas as pd


from django.core.exceptions import ValidationError


# Formulario para la creación de usuarios

class UserRegisterForm(forms.ModelForm):


    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña',
                'class':'form-control '
            }
        )

    )
    password2 = forms.CharField(
        label='Confirme contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña',
                'class':'form-control '
            }
        )

    )

    class Meta:

        model = User
        fields = ('__all__')
        exclude =['password','last_login', 'is_superuser', 'is_active','is_staff']
        
        widgets={


        'codigo' :NumberInput(
            attrs={
                'class':'form-control ',
                 'id':'cedula'
            }
        ),
    

        'username' :TextInput(
            attrs={
                'autocomplete': 'off',
                'class':'form-control '
            }
        ),
        

        'email' : EmailInput(
            attrs={
                'autocomplete': 'off',
                'class':'form-control '
            }
        )
        
    }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

class PeriodoForm(forms.Form):

    Año = forms.CharField(
        label='Año',
        required=True,
        widget=forms.NumberInput()

    )

    periodo = forms.CharField(
        label='periodo',
        required=True,
        widget=forms.NumberInput()

    )

    def clean_periodo(self):
        ano = self.cleaned_data.get('Año')
        periodo = self.cleaned_data.get('periodo')
        concat=str(ano) + "-" + periodo
        
        if Periodos.objects.filter(periodo = concat).exists() :
           self.add_error('Año', 'El periodo que intenta crear ya existe.')
        else:
            return concat

class ProgramaForm(forms.ModelForm):

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Programas
        fields = ('__all__')
        exclude =['an_creacion', 'is_active', 'cod_prog', 'is_active' ]



        widgets={

            'programa_name': TextInput(
                attrs={
                    'placeholder':"Ingrese un nombre",
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),
            'costo': HiddenInput(),
             'tipe': Select(
                attrs={
                    'id':'Tipo_program',
                    'class':'form-control'
                }
            ),


        }

    
    
    def clean_programa_name(self):

        nombre = str(self.cleaned_data.get('programa_name'))

        return nombre.title()

class PensumRegisterForm(forms.ModelForm):

    class Meta:
        model = Pensum
        fields = ('__all__')
        exclude =['an_creacion']


#Formulario destinado a la creación de docentes está ok
class TeacherForm(forms.ModelForm):


    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Docente
        fields = ('__all__')
        exclude =['fecha_reg', 'is_active']

        widgets={

            'nacimiento': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),

             'tDocument': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),

            'codigo': NumberInput(
                attrs={
                    'autofocus': True,
                    'placeholder':"Ingrese el documento",
                    'autocomplete': 'off',
                    'class':'form-control',
                    "onkeydown":"noPuntoComa( event )",
                    'id':'cedula'
                    
                }
            ),
            'nombres': TextInput(
                attrs={
                    'placeholder':"Ingrese nombres",
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder':"Ingrese apellidos",
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder':"nombre de usuario",
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),
            

            'direccion': TextInput(
                attrs={
                    'placeholder':"nombre dirección",
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),

            'telefono': NumberInput(
                attrs={
                    'placeholder':"Ingrese teléfono",
                    'autocomplete': 'off',
                    'class':'form-control',
                    "onkeydown":"noPuntoComa( event )"
                }
            ),

            'email': EmailInput(
                attrs={
                    'placeholder':"Ingrese correo electrónico",
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),
            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),

        }
    
    def clean_nombres(self):

        nombre = str(self.cleaned_data.get('nombres'))

        return nombre.title()

    def clean_apellidos(self):

        nombre = str(self.cleaned_data.get('apellidos'))

        return nombre.title()
    

#Formulario destinado al cargue de notas de los estudiantes.
class UploadForm(forms.Form):

    corte = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'name': 'corte',
                'id': 'corteFull'
            }
        )

    )

    archivo = forms.FileField(
       required=True,
        widget=forms.FileInput(
            attrs={
                'class':'form-control',
                'name': 'archivo',
                'id': 'archivo',
            }
        )
    )

    asignatura = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'name': 'asignatura',
                'id': 'asignatura'
            }
        )

    )


class PeriodoForm(forms.Form):

    Año = forms.CharField(
        label='Año',
        required=True,
        widget=forms.NumberInput()

    )

    periodo = forms.CharField(
        label='periodo',
        required=True,
        widget=forms.NumberInput()

    )

    def clean_periodo(self):
        ano = self.cleaned_data.get('Año')
        periodo = self.cleaned_data.get('periodo')
        concat=str(ano) + "-" + periodo
        
        if Periodos.objects.filter(periodo = concat).exists() :
           self.add_error('Año', 'El periodo que intenta crear ya existe.')
        else:
            return concat

class MateriasForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super (MateriasForm,self ).__init__(*args,**kwargs)
        self.fields['docente'].queryset = Docente.objects.filter(is_active = True)
    
    
    

    class Meta:
        model = Materias
        fields = ('__all__')
        exclude =['an_creacion', 'is_active', 'codigo']

        widgets={

                'materia': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'materia'

                    }
                ),
                'programa': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'carrera'

                    }
                ),
                'sede': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'sede'

                    }
                ),
                'pensum_asig': Select(
                    attrs={
                        'class':'form-select ',
                        'id': 'pensum_asig'

                    }
                ),

                'periodo': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select '
                    }
                ),
                'docente': Select(
                    
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select '
                    }
                ),
                
        }

    

    def clean_codigo(self):
        b = (self.cleaned_data.get('codigo'))
        if b[0] == "0":
            self.add_error('codigo', 'El código no puede iniciar por cero')
        else:
            return b
    
class InventarioRegisterForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = ('__all__')
        exclude =['an_creacion']

        widgets={

                'programa': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'carrera'

                    }
                ),

                'pensum_asig_inv': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'pensum_asig'

                    }
                ),
                
                
        } 

class StudentRegisterForm(forms.ModelForm):

    
    class Meta:
        """Meta definition for MODELNAMEform."""
        
        model = Estudiante
        fields = ('__all__')
        exclude =['is_estudiante','is_active', 'fecha_reg', 'is_matriculado','codigo', 'is_graduado', 'costo_cierre']
        
        widgets={

            'cedula': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id':'cedula'
                }
            ),
            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-select '
                }
            ),
            'periodo_matriculado': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-select '
                }
            ),
            
            'nacionalidad': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-select '
                }
            ),
            'carrera': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-select ',
                    'id':'carrera'
                }
            ),
            'malla': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-select ',
                    'id':'malla'
                }
            ),
            'sede': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'sede'

                    }
                ),
            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-select '
                }
            ),

            'nacimiento': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'nombre': TextInput(
                attrs={
                    'placeholder':"Ingrese nombres",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nombre'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder':"Ingrese apellidos",
                    'autocomplete': 'off',
                    'class':'form-control '
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder':"nombre de usuario",
                    'autocomplete': 'off',
                    'class':'form-control '
                }
            ),

            'direccion': TextInput(
                attrs={
                    'placeholder':"nombre dirección",
                    'autocomplete': 'off',
                    'class':'form-control '
                }
            ),

            'telefono': TextInput(
                attrs={
                    'placeholder':"Ingrese teléfono",
                    'autocomplete': 'off',
                    'class':'form-control '
                }
            ),

            'email': EmailInput(
                attrs={
                    'placeholder':"Ingrese correo electrónico",
                    'autocomplete': 'off',
                    'class':'form-control '
                }
            ),
            'nombre_acudiente': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control '
                }
            ),
            'apellidos_acudiente': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control '
                }
            ),
            'telefono_acudiente': TextInput(
                attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control '
                }
            ),

            'cedula_acudiente': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control '
                }
            ),
            'masivo': CheckboxInput(
                attrs={
                    'id': 'masivo'
                }
            ),


        }
    
    def clean_nombre(self):

        nombre = str(self.cleaned_data.get('nombre'))

        return nombre.title()


    def clean_apellidos(self):

        nombre = str(self.cleaned_data.get('apellidos'))

        return nombre.title()
    
    def clean_nombre_acudiente(self):
        nombre = str(self.cleaned_data.get('nombre_acudiente'))

        return nombre.title()

    def clean_apellidos_acudiente(self):
        nombre = str(self.cleaned_data.get('apellidos_acudiente'))

        return nombre.title()

    
    def clean_cedula(self):
        b = str(self.cleaned_data.get('cedula'))
        if b[0] == "0":
            self.add_error('cedula', 'La cédula no puede iniciar por cero')
        else:
            return b

    def clean_cedula_acudiente(self):
        b = str(self.cleaned_data.get('cedula_acudiente'))
        if b[0] == "0":
            self.add_error('cedula_acudiente', 'La cédula no puede iniciar por cero')
        else:
            return b
 
    def clean_telefono(self):
        tamaño = len(self.cleaned_data.get('telefono'))
        tamaño_valor = self.cleaned_data.get('telefono')
        if tamaño == 7 or tamaño == 10 :
           return tamaño_valor
            
        else:
            self.add_error('telefono', 'El teléfono debe de tener 7 o 10 números')
    
    def clean_telefono_acudiente(self):
        tamaño = len(self.cleaned_data.get('telefono_acudiente'))
        tamaño_valor = self.cleaned_data.get('telefono_acudiente')
        if tamaño == 7 or tamaño == 10 :
           return tamaño_valor
            
        else:
            self.add_error('telefono', 'El teléfono debe de tener 7 o 10 números')

    
    def clean_nacimiento(self):
        fecha_inicial = self.cleaned_data.get('nacimiento')
        fecha_actual = date.today()
        fecha_final = ((fecha_actual - fecha_inicial).days)/365
        
        if fecha_final <= 13 :
           self.add_error('nacimiento', 'El Estudiante no puede tener menos de 13 años')
        else:
            return fecha_inicial


class StudentAsigMate(forms.Form):

    carga = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'class':'form-control '
            }
        )
    )

    def clean_carga(self):
        carga_file1 = self.cleaned_data['carga'].name
        carga_file_exp = (self.files['carga'])

        if carga_file1 != 'cargue_estudiantes.xlsx' :
           self.add_error('carga', 'Archivo inválido, recuerde que el archivo tiene por nombre "cargue_estudiantes.xlsx" , por favor verifique y cárguelo nuevamente')

        else:
            return carga_file_exp