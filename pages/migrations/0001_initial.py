# Generated by Django 4.2.5 on 2023-10-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Grado', models.CharField(max_length=100)),
                ('Correo', models.EmailField(max_length=254)),
                ('Contraseña', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]