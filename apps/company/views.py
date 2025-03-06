from django.shortcuts import render
from rest_framework import viewsets

from apps.company.models import (Company, 
                     CompanyResponsiblePerson)
from apps.company.serializers import (CompanySerializer, 
                          CompanyResponsiblePersonSerializer)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyResponsiblePersonViewSet(viewsets.ModelViewSet):
    queryset = CompanyResponsiblePerson.objects.all()
    serializer_class = CompanyResponsiblePersonSerializer
