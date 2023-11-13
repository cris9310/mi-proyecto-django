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
                    'class':'form-control',
                    'id': 'nacimiento'
                }
            ),
            'nacionalidad': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nacionalidad'
                }
            ),

             'tDocument': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    "id": "tDocument"
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
                    'class':'form-control',
                    'id': 'nombres'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder':"Ingrese apellidos",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'apellidos'
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder':"nombre de usuario",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'username'
                }
            ),
            

            'direccion': TextInput(
                attrs={
                    'placeholder':"nombre dirección",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'direccion'
                }
            ),

            'telefono': NumberInput(
                attrs={
                    'placeholder':"Ingrese teléfono",
                    'autocomplete': 'off',
                    'class':'form-control',
                    "onkeydown":"noPuntoComa( event )",
                    'id': 'telefono',
                }
            ),

            'email': EmailInput(
                attrs={
                    'placeholder':"Ingrese correo electrónico",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'email',
                }
            ),
            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'sexo'
                }
            ),

        }
    
    def clean_nombres(self):

        nombre = str(self.cleaned_data.get('nombres'))

        return nombre.title()

    def clean_apellidos(self):

        nombre = str(self.cleaned_data.get('apellidos'))

        return nombre.title()
    
    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get('username')):
           
           self.add_error('username', 'Este usuario ya se encuentra creado')
        else:
           return self.cleaned_data.get('username')

# Formulario para la actualización de los datos del docente
class TeacherUpdateForm(forms.ModelForm):


    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Docente
        fields = ('__all__')
        exclude =['fecha_reg', 'is_active', 'username']

        widgets={

            'nacimiento': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class':'form-control',
                    'id': 'nacimiento'
                }
            ),
            'nacionalidad': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nacionalidad'
                }
            ),

             'tDocument': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    "id": "tDocument"
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
                    'class':'form-control',
                    'id': 'nombres'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder':"Ingrese apellidos",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'apellidos'
                }
            ),
            

            'direccion': TextInput(
                attrs={
                    'placeholder':"nombre dirección",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'direccion'
                }
            ),

            'telefono': NumberInput(
                attrs={
                    'placeholder':"Ingrese teléfono",
                    'autocomplete': 'off',
                    'class':'form-control',
                    "onkeydown":"noPuntoComa( event )",
                    'id': 'telefono',
                }
            ),

            'email': EmailInput(
                attrs={
                    'placeholder':"Ingrese correo electrónico",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'email',
                }
            ),
            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'sexo'
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
        
        model = Estudiante
        fields = ('__all__')
        exclude =['is_estudiante','is_active', 'fecha_reg', 'is_matriculado','codigo', 'is_graduado', 'costo_cierre', "masivo", "updated_at"]
        
        widgets={

            'cedula': NumberInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id':'cedula',
                    'placeholder':"Ingrese número de documento",
                    "onkeydown":"noPuntoComa( event )"
                }
            ),
            'tDocument': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    "id": "tDocument"
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
                    'class':'form-control ',
                    'id': 'apellidos'
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder':"Ingrese dirección",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'direccion'
                }
            ),

            'telefono': NumberInput(
                attrs={
                    'placeholder':"Ingrese teléfono",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'telefono',
                    "onkeydown":"noPuntoComa( event )"
                }
            ),

            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'sexo'
                }
            ),
            'nacionalidad': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nacionalidad'
                }
            ),
            'nacimiento': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class':'form-control',
                    'id': 'nacimiento'
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder':"Ingrese correo electrónico",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'email'
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder':"Ingrese un nombre de usuario",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'username'
                }
            ),

            'nombre_acudiente': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'placeholder':"Ingrese nombre del acudiente",
                    'id': 'nombre_acudiente'
                }
            ),
            'apellidos_acudiente': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'placeholder':"Ingrese apellidos del acudiente",
                    'class':'form-control ',
                    'id': 'apellidos_acudiente'

                }
            ),
            'telefono_acudiente': NumberInput(
                attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'placeholder':"Ingrese teléfono de contacto",
                    'id': 'telefono_acudiente',
                    "onkeydown":"noPuntoComa( event )"


                }
            ),

            'cedula_acudiente': NumberInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'placeholder':"Ingrese documento del acudiente",
                    'id': 'cedula_acudiente',
                    "onkeydown":"noPuntoComa( event )"


                }
            ),


            'periodo_matriculado': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'periodo_matriculado'

                }
            ),
            
            'carrera': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id':'carrera'
                }
            ),
            'pensum_asig': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id':'pensum_asig'
                }
            ),
            'sede': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-control ',
                        'id': 'sede'

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
    
    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get('username')):
           
           self.add_error('username', 'Este usuario ya se encuentra creado')
        else:
           return self.cleaned_data.get('username')

class StudentAsigMate(forms.Form):

    carga = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'class':'form-control ',
                'name':'carga',
                'id':'carga'

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
        
class GraduateRegisterForm(forms.ModelForm):

    concat = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'class':'form-control',
                'id':'concat',
                'name':'concat',
            }
        )

    )

    
    class Meta:
        
        model = Graduated
        fields = ('__all__')
        exclude =['student','carrera', 'periodo_grado', 'fecha_reg']

        widgets={

            'libro': NumberInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id':'libro',
                    'name':'libro',
                    'placeholder':"Ingrese número de libro",
                }
            ),
            'folio': NumberInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id':'folio',
                    'name':'folio',
                    'placeholder':"Ingrese número de folio",
                }
            ),
        }