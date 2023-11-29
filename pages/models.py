from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario =models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Grado = models.CharField(max_length=100)
    Correo = models.EmailField()
    Contraseña =models.CharField(max_length=100)
    class Meta:
        managed = False  # Indica que no se gestionará la creación de la tabla
        db_table = 'usuario'  # Especifica el nombre de la tabla existente

    def __str__(self):
        return self.Nombre