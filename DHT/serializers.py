from rest_framework import serializers
from .models import Patient
class DHT11serialize(serializers.ModelSerializer):
      class Meta :
            model = Patient
            fields ='__all__'
