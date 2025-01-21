from rest_framework import serializers
from .models import Company, CompanyResponsiblePerson

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyResponsiblePersonSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()  # Display the company name in the API

    class Meta:
        model = CompanyResponsiblePerson
        fields = '__all__'
