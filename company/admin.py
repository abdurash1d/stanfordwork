from django.contrib import admin

from .models import (Company, 
                     CompanyResponsiblePerson)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'locations', 'created_at')
    search_fields = ('name', 'phone_number', 'email', 'locations')
    list_filter = ('created_at',)

@admin.register(CompanyResponsiblePerson)
class CompanyResponsiblePersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'phone_number', 'email', 'company')
    search_fields = ('full_name', 'position', 'phone_number', 'email')
    list_filter = ('company',)
