from django.contrib import admin
from .models.carrera import Carrera
#from .models import Carrera

@admin.register(Carrera)

class CarreraAdmin(admin.ModelAdmin):
     list_display=("nombre", "descripcion")