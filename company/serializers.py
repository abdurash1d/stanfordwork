from rest_framework import serializers

from .models import (Company, 
                     CompanyResponsiblePerson)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyResponsiblePersonSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField() 

    class Meta:
        model = CompanyResponsiblePerson
        fields = '__all__'
