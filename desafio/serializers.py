from rest_framework import serializers
from desafio.models import Video, Categoria

from desafio import validators


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'
    
    cor = serializers.CharField(style={'input_type': 'color'})

    def validate(self, data):
        if not validators.is_valid_categoria_titulo(data.get('titulo', '')):
            raise serializers.ValidationError('O campo é obrigatório')
        if not validators.is_valid_cor(data.get('cor')):
            raise serializers.ValidationError('"Formato de cor inválido. Use #RRGGBB (ex: #FF0000)."')

        return data
