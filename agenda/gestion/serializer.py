from rest_framework import serializers
from .models import Tareas, Etiqueta


class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=40, trim_whitespace=True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(max_length= 8, min_length= 8, regex="[0-9]")
    #dni = serializers.IntegerField(min_value=1000000, max_value=999999)
    pass

class TareasSerializer(serializers.ModelSerializer):
    foto= serializers.CharField(max_length=100)

    class Meta: 
        model = Tareas
        fields = '__all__'
        extra_kwargs= {
            'etiquetas': {
                'write_only' : True
            }
        }
        

class TareaSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Tareas
        fields = '__all__'
        depth = 1



class EtiquetaSerializer(serializers.ModelSerializer):
    #variable = serializers.CharField(read_only=True)
    tareas = TareaSerializer(many=True, read_only=True)#, source='tareas')
    #otra_variable= serializers.EmailField()

    class Meta: 
        model = Etiqueta
        fields = '__all__'
        extra_kwargs = {
            #'nombre' : {'write_only': True},
            'id' : {'read_only': True}
        }
        read_only_fields = ['createAt']
        
        

class TareaPersonalizableSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Tareas
        fields = '__all__'
        # exclude = ['nombre'] # funciona tanto para lectura como escritura
        extra_kwargs = {
            'nombre': {
                'read_only': True
            }
        }

class ArchivoSerializer(serializers.Serializer):
    archivo= serializers.ImageField(max_length=100, use_url=True)


class EliminarArchivoSerializer(serializers.Serializer):
    archivo = serializers.CharField(max_length=100)
        