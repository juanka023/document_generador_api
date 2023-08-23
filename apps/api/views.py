from rest_framework.views import APIView
from rest_framework.response import Response
from django.template import Context, Template
from docx import Document as DocxDocument
import io
from django.core.files.temp import NamedTemporaryFile
from .models import DocumentData

class DocumentGenerationView(APIView):
    template_text = "Se remite a Sr(a) {{nombre}} la disposición de presentarse en la entidad {{entidad}} con su vehículo de placa {{placa}}."

    def post(self, request, *args, **kwargs):
        data = request.data
        nombre = data.get('nombre', '')
        placa = data.get('placa', '')
        entidad = data.get('entidad', '')

        context = Context({
            'nombre': nombre,
            'placa': placa,
            'entidad': entidad,
        })

        template = Template(self.template_text)
        generated_text = template.render(context)

        plain_text_file = io.BytesIO()
        plain_text_file.write(generated_text.encode('utf-8'))
        plain_text_file.seek(0)

        # Create a NamedTemporaryFile for plain text content
        with NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(plain_text_file.read())
            temp_file.seek(0)
            
            generated_document = DocumentData.objects.create(
                nombre=nombre,
                placa=placa,
                entidad=entidad,
                archivo_texto=temp_file
            )

        docx_file = io.BytesIO()
        doc = DocxDocument()
        doc.add_paragraph(generated_text)
        doc.save(docx_file)
        docx_file.seek(0)

        # Create a NamedTemporaryFile for DOCX content
        with NamedTemporaryFile(delete=True, suffix='.docx') as docx_temp_file:
            docx_temp_file.write(docx_file.read())
            docx_temp_file.seek(0)

            generated_document.archivo_docx.save(f'{nombre}_docx.docx', docx_temp_file)

        response_data = {
            'plain_text': "success",
        }

        return Response(response_data)
