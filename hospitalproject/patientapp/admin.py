from django.contrib import admin
from patientapp.models import patientb

# Register your models here.

class patientbAdmin(admin.ModelAdmin):
    list_display=("name","address","date","department","disease")
    ordering=("name","address","date","department","disease")
    search_fields=("name","address","date","department","disease")

admin.site.register(patientb,patientbAdmin)

