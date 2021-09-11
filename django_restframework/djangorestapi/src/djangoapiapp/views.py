from django.shortcuts import render
from rest_framework import response
# from rest_framework import serializers
# from rest_framework.serializers import Serializer
from .models import employee
from django.http import HttpResponse, request
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import employeeSerializers
from djangoapiapp import serializers

# Create your views here.

class employeeList(APIView):

    def get(self, request, *args, **kwargs):
        employee1 = employee.objects.all()
        serializer = employeeSerializers(employee1, many=True)
        return Response(serializer.data)

    def post(self,request,*args, **kwargs):
        serializer = employeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
