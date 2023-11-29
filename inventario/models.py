from django.db import models

# Create your models here.

##no se utiliza pk por que se crea automaticamente gracias a la opcion AI auto increment
class ElementoEnUso(models.Model):
    idElementoEnUso =models.AutoField(primary_key=True)
    Fecha = models.DateField()  # Campo para almacenar la fecha
    Usuario_idUsuario = models.PositiveIntegerField()
    class Meta:
        managed = False  # Indica que no se gestionará la creación de la tabla
        db_table = 'elementoenuso'  # Especifica el nombre de la tabla existente

    def __str__(self):
        return self.Fecha
    
class ElementoPrestado(models.Model):
    idElementoPrestado =models.AutoField(primary_key=True)
    Fecha = models.DateField()  # Campo para almacenar la fecha
    Encargado = models.CharField(max_length=100)
    Usuario_idUsuario = models.PositiveIntegerField()
    class Meta:
        managed = False  # Indica que no se gestionará la creación de la tabla
        db_table = 'elementoprestado'  # Especifica el nombre de la tabla existente

    def __str__(self):
        return self.Encargado
    
class Elementos(models.Model):
    idElementos =models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    Observaciones = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)
    Cantidad = models.PositiveIntegerField()
    Ubicación = models.CharField(max_length=100)
    ElementoEnUso_idElementoEnUso = models.PositiveIntegerField()
    Alertas_idAlertas = models.PositiveIntegerField()
    ElementoPrestado_idElementoPrestado = models.PositiveIntegerField()
    class Meta:
        managed = False  # Indica que no se gestionará la creación de la tabla
        db_table = 'elementos'  # Especifica el nombre de la tabla existente

    def __str__(self):
        return self.Nombre
    
class Alertas(models.Model):
    idAlertas =models.AutoField(primary_key=True)
    Tipo = models.CharField(max_length=100)
    Fecha = models.DateField()  # Campo para almacenar la fecha
    Mensaje = models.CharField(max_length=100)
    class Meta:
        managed = False  # Indica que no se gestionará la creación de la tabla
        db_table = 'alertas'  # Especifica el nombre de la tabla existente

    def __str__(self):
        return self.Tipo