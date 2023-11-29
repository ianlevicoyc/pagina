from django.contrib import admin
from .models import ElementoEnUso, ElementoPrestado, Elementos, Alertas

admin.site.register(ElementoEnUso)
admin.site.register(ElementoPrestado)
admin.site.register(Elementos)
admin.site.register(Alertas)