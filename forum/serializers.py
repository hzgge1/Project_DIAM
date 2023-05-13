from rest_framework import serializers
from .models import Questao

class QuestaoSerializer(serializers.ModelSerializer):
    class Meta: #(1)
        model = Questao
        fields = ('pk', 'user', 'questao_titulo', 'questao_descricao', 'questao_data', 'numero_likes', 'tags')