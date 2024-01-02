from rest_framework import serializers
from .models import LanguageModels


class RoomBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = LanguageModels
        fields = '__all__'
