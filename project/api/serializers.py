from rest_framework import serializers
from api.models import Blood_Bank

class Blood_Bank_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blood_Bank
        fields = "__all__"