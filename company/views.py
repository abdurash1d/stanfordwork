from django.shortcuts import render
from rest_framework import viewsets

from .models import (Company, 
                     CompanyResponsiblePerson)
from .serializers import (CompanySerializer, 
                          CompanyResponsiblePersonSerializer)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyResponsiblePersonViewSet(viewsets.ModelViewSet):
    queryset = CompanyResponsiblePerson.objects.all()
    serializer_class = CompanyResponsiblePersonSerializer
