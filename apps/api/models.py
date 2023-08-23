from django.db import models

class DocumentData(models.Model):
    nombre = models.CharField(max_length=250)
    placa = models.CharField(max_length=20)
    entidad = models.CharField(max_length=250)
    archivo_texto = models.FileField(upload_to='documents', blank=True, null=True)
    archivo_docx = models.FileField(upload_to='documents', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'