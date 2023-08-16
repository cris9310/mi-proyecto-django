import random
import datetime
from .models import *




class generador():
    
    def code_materias_generator():

        try:
            filtro = Materias.objects.latest('id').codigo
            cod_asign = int(filtro) + 1
            return cod_asign
        except:
            año = datetime.now()
            cod_asign= str(año.year) + str("01")
            return str(cod_asign)




