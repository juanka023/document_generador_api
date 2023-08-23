from django.contrib import admin
from .models import DocumentData

@admin.register(DocumentData)
class DocumentDataAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'placa', 'entidad')