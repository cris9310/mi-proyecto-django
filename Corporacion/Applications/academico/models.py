from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from datetime import datetime


from .choices import *
from datetime import datetime
from .funciones import * 
from .manager import *
from .validators import *

#Con estos primeros 4 modelos lo que hacemos es crear catálogos para los choices y hacer la app más escalable
class CatalogsTypesProg(models.Model):
    tipo = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self): 
        return  self.tipo

class CatalogsTypesDocuement(models.Model):
    tipo = models.CharField(max_length=200, null=False, blank=False)
    nombre = models.CharField(max_length=200, null=False, blank=False)


    def __str__(self): 
        return  self.nombre
    
class CatalogsTypesGen(models.Model):
    genero = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self): 
        return  self.genero


class CatalogsTypesRol(models.Model):
    rol = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self): 
        return  self.rol

class CatalogsSede(models.Model):
    sede= models.CharField(max_length=200, null=False, blank=False)

    def __str__(self): 
        return  self.sede


#Modelo de los usuarios, se reescribió todo el modelo inicial e hicimos uno desde cero, logueamos con user y contraseña
class User(AbstractBaseUser):
    codigo=models.CharField(primary_key=True, max_length=20, unique=True, verbose_name='Código')
    nombres = models.CharField(max_length=50, blank=False, null=True)
    apellidos = models.CharField(max_length=50, blank=False, null=True)
    username=models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name='Usuario')
    email=models.EmailField( verbose_name='Em@il', blank=False)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    tipe = models.ForeignKey(CatalogsTypesRol, on_delete=models.CASCADE)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= ['codigo', ]
    objects= UserManager()

    def get_short_name(self):
        return self.username

    class Meta:
        ordering = ('-created_at', '-updated_at', )
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    

class Periodos(models.Model):
    periodo = models.CharField(max_length=15, unique=True, blank=False, null=False)
    an_creacion=models.CharField(max_length=50, default=datetime.now()) 
    objects = periodoManager()

    def __str__(self): 
        return self.periodo
    
    class Meta:
       ordering = ('-an_creacion', )

class Programas(models.Model):
    cod_prog=models.CharField(max_length=10, unique=True, verbose_name='Código del Programa')
    programa_name=models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre del Programa')
    aceptado = models.PositiveIntegerField(null=False, blank=False, verbose_name='Total materias para grado')
    matricula = models.DecimalField(max_digits= 25, decimal_places=0, default=0)
    cuota_valor= models.DecimalField(max_digits= 25, decimal_places=0, default=0)
    cuotas= models.PositiveIntegerField(null=False, blank=False, verbose_name='Numero de cuotas')
    costo =  models.DecimalField(max_digits= 25, decimal_places=0, default=0)
    an_creacion=models.CharField(max_length=50, default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    tipe = models.ForeignKey(CatalogsTypesProg, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    objects = BuscadorManager()


    def __str__(self): 
        return self.programa_name 

class Pensum(models.Model):
    programa = models.ForeignKey(Programas, on_delete=models.CASCADE)
    malla = models.PositiveIntegerField(null=False, blank=False)
    an_creacion=models.CharField(max_length=50, default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self): 
        return  str(self.malla)

class Inventario(models.Model):

    nombre_materia = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nombre de la Asignatura')
    programa = models.ForeignKey(Programas, on_delete=models.CASCADE)
    pensum_asig_inv = models.ForeignKey(Pensum, on_delete=models.CASCADE )
    an_creacion=models.CharField(max_length=50, default=datetime.now()) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return  self.nombre_materia

class Docente(models.Model):
    tDocument = models.ForeignKey(CatalogsTypesDocuement, on_delete=models.CASCADE, verbose_name='Tipo de documento')
    codigo = models.CharField(unique=True, max_length=20, verbose_name='Número de cédula', validators=[validate_cero])
    nombres = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombres')
    apellidos = models.CharField( max_length=100, blank=False, null=False, verbose_name='Apellidos')
    username=models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name='Usuario', validators=[validate_blanco])
    direccion = models.CharField( max_length=50, blank=False, null=False, verbose_name='dirección')
    nacionalidad=models.CharField( verbose_name='Nacionalidad',max_length=100, choices=COUNTRIES, default="Colombia" )
    nacimiento = models.DateField(verbose_name='Fecha de nacimiento', validators=[validate_nacimiento])
    sexo=models.CharField( verbose_name='Género',max_length=50, choices=GENEROS, default="Femenino")
    telefono = models.CharField(max_length=10, verbose_name='Teléfono', validators=[validate_telefono])
    email = models.EmailField() 
    fecha_reg=models.DateField(default=datetime.now(), verbose_name='Fecha')
    is_active=models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
    objects = BuscadorManager()

    def __str__(self): 
        return self.nombres + " " + self.apellidos
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha_reg = datetime.now()
        self.updated_at = datetime.now()
        return super(Docente, self).save(*args, **kwargs)

class Materias(models.Model):

    codigo = models.PositiveIntegerField(null=False, blank=False, verbose_name='Código')
    programa = models.ForeignKey(Programas, on_delete=models.CASCADE)
    pensum_asig = models.ForeignKey(Pensum, on_delete=models.CASCADE )
    materia  = models.ForeignKey(Inventario, on_delete=models.CASCADE )
    sede=models.ForeignKey(CatalogsSede, verbose_name='Sede', on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE )
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)
    an_creacion=models.CharField(max_length=50, default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    objects = BuscadorManager()


    class Meta:
        ordering = ['codigo']
    
    def __str__(self): 
        return self.materia

class Estudiante(models.Model):
    codigo = models.CharField(unique=True, max_length=50, verbose_name='código')
    tDocument = models.ForeignKey(CatalogsTypesDocuement, on_delete=models.CASCADE, verbose_name='Tipo de documento')
    cedula = models.CharField(unique=False, max_length=20, verbose_name='Identificación del Estudiante', validators=[validate_cero])
    nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombres')
    apellidos=models.CharField( verbose_name='Apellidos', max_length=100, blank=False, null=False)
    nacionalidad=models.CharField( verbose_name='Nacionalidad',max_length=100, choices=COUNTRIES, default="Colombia" )
    telefono=models.CharField( verbose_name='Teléfono', max_length=10, blank=False, null=False, validators=[validate_telefono])
    direccion=models.CharField( verbose_name='Direccion', max_length=50, blank=False, null=False)
    nacimiento=models.DateField( verbose_name='Fecha de Nacimiento', validators=[clean_nacimiento2])
    carrera=models.ForeignKey(Programas, verbose_name='Programa', on_delete=models.CASCADE)
    costo_cierre = models.DecimalField(max_digits= 25, decimal_places=0, default=0)
    pensum_asig = models.ForeignKey(Pensum, verbose_name='pensum_asig', on_delete=models.CASCADE)
    email=models.EmailField( verbose_name='Em@il', blank=False, unique=False)
    sexo=models.CharField( verbose_name='sexo',max_length=50, choices=GENEROS, default="Femenino")
    sede=models.ForeignKey(CatalogsSede, verbose_name='Sede', on_delete=models.CASCADE)
    periodo_matriculado=models.ForeignKey(Periodos, verbose_name='Periodo', on_delete=models.CASCADE)
    fecha_reg=models.DateField(default=datetime.now(), verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True)
    username=models.CharField(max_length=50, blank=False, null=False, verbose_name='Usuario', unique=True)
    nombre_acudiente = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombres del acudiente')
    apellidos_acudiente =models.CharField( verbose_name='Apellidos del acudiente', max_length=100, blank=False, null=False)
    telefono_acudiente =models.CharField( verbose_name='Teléfono del acudiente', max_length=10, blank=False, null=False, validators=[validate_telefono])
    cedula_acudiente =models.CharField(unique=False, max_length=20, verbose_name='Cédula del acudiente', validators=[validate_cero])
    document=models.BooleanField( default=False)
    simat=models.BooleanField(default=False)
    siet=models.BooleanField(default=False)
    actaBachillerato=models.BooleanField(default=False)
    fotos=models.BooleanField( default=False)
    serviciosPublicos=models.BooleanField(default=False)
    carneSalud=models.BooleanField(default=False)
    cedulaAcudiente=models.BooleanField( default=False)
    certificados=models.BooleanField(default=False)
    homologacion=models.BooleanField(default=False)
    observaciones=models.CharField(max_length=100, blank=True, null=True, verbose_name='Observacion')
    is_active=models.BooleanField(default=True)
    is_estudiante=models.BooleanField(default=True)
    is_matriculado=models.BooleanField(default=False)
    is_graduado=models.BooleanField(default=False)
    masivo=models.BooleanField(default=False)
    objects=UserManager()
    objects = BuscadorManager()
    
    def __str__(self): 
        
        return "{0}, {1}".format(self.apellidos, self.nombre)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha_reg = datetime.now()
        self.updated_at = datetime.now()
        return super(Estudiante, self).save(*args, **kwargs)
    

class Banner(models.Model):
    cod_student = models.ForeignKey(Estudiante, verbose_name='Estudiante', on_delete=models.CASCADE)
    Programa = models.ForeignKey(Programas, verbose_name='Programa', on_delete=models.CASCADE)
    materia = models.ForeignKey(Materias, verbose_name='Materias', on_delete=models.CASCADE)
    corte1 = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name='corte 1', validators=[validate_decimal])
    corte2 = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name='corte 2', validators=[validate_decimal])
    corte3 = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name='corte 3', validators=[validate_decimal])
    promedio = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name='promedio')
    objects = BuscadorManager()
    
   
    class Meta:
        ordering = ['materia__materia']
    
class Graduated(models.Model):
    student = models.ForeignKey(Estudiante, verbose_name='Estudiante', on_delete=models.CASCADE)
    carrera = models.ForeignKey(Programas, verbose_name='Programa', on_delete=models.CASCADE)
    periodo_grado = models.CharField(max_length=15, blank=False, null=False)
    libro = models.PositiveIntegerField(null=False, blank=False, verbose_name='Libro')
    folio = models.PositiveIntegerField(null=False, blank=False, verbose_name='Folio')
    fecha_reg=models.DateField(default=datetime.now(), verbose_name='Fecha')

    objects = BuscadorManager()

    def __str__(self): 
        
        return "{0}, {1}".format(self.student.nombre, self.student.apellidos)

   
class Habilitaciones(models.Model):
    C1 = models.BooleanField(default=False)
    C2 = models.BooleanField(default=False)
    C3 = models.BooleanField(default=False)
    CF = models.BooleanField(default=False)
    B1 = models.BooleanField(default=False)
    B2 = models.BooleanField(default=False)
    B3 = models.BooleanField(default=False)
    Cerrado = models.BooleanField(default=False)


class Acciones(models.Model):
    usuario = models.CharField(max_length=100, blank=False, null=False, verbose_name='Usuario')
    nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombres')
    accion = models.CharField(max_length=100, blank=False, null=False, verbose_name='accion')
    fecha_reg = models.DateField(default=datetime.now(), verbose_name='Fecha')



