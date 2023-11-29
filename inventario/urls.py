from django.urls import path

from . import views


urlpatterns = [

    path('EnUso', views.form_ElementoEnUso, name='EnUso'),
    path('prestado', views.form_ElementoPrestado, name='prestado'),
    path('elemento', views.form_Elemento, name='elemento'), 
    path('alertas', views.form_Alertas, name='alertas')
] 