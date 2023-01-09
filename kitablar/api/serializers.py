from rest_framework import serializers
from kitablar.models import Kitab, Yorum 



class YorumSerializer(serializers.ModelSerializer):
    yorum_sahibi = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Yorum
        # fields = "__all__"
        exclude = ['kitab']


class KitabSerializer(serializers.ModelSerializer):
    yorumlar = YorumSerializer(many=True, read_only=True)
    class Meta:
        model = Kitab 
        fields = "__all__"




