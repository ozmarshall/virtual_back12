from tkinter.messagebox import NO
from django.db import models
from cloudinary import models as modelsCloudinary

class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    foto = modelsCloudinary.CloudinaryField(folder='plato')
    disponible = models.BooleanField(default=True, null=False)
    precio = models.FloatField(null=False)

    class Meta:
        db_table = 'platos'


    

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=False)
    cantidad = models.IntegerField(null=False)
    precio_diario = models.FloatField(null=False)
    platoId = models.ForeignKey(to=Plato, related_name='stock', on_delete=models.CASCADE, db_column='plato_id')

    class Meta:
        db_table = 'stocks'
        unique_together=[['fecha', 'platoId']]
        
