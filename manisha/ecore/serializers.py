from rest_framework import serializers

from ecore.models import Marchent, Lenin, RFID


class MarchentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marchent
        fields = '__all__'
class LeninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lenin
        fields = '__all__'
class RFIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFID
        fields = '__all__'

