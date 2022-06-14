from django.shortcuts import render
from api.serializers import Blood_Bank_Serializer
from api.models import Blood_Bank
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class index(APIView):
    def get(self, request):
        blood_bank=Blood_Bank.objects.all()
        serializer=Blood_Bank_Serializer(blood_bank,many=True)
        return Response(serializer.data)
