from rest_framework import serializers
from .models import Top100

class Top100Serializer(serializers.ModelSerializer):
    class Meta:
        model = Top100 # 모델 설정
        fields = ('id','title','artist','genre','image') # 필드 설정
