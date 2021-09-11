from django.db.models import fields
from rest_framework import serializers
from .models import employee
from rest_framework.fields import ModelField

class employeeSerializers(serializers.Serializer):

    class Meta:
        model = employee
        fields = '__all__'
        # fields = ("first_name","last_name")
