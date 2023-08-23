import io
import zipfile
from docx import Document
from django.http import HttpResponse
from django.template import Context, Template
from rest_framework.views import APIView

class DocumentGenerationView(APIView):
    def post(self, request):
        data = request.data
        nombre = data.get('nombre', '')
        placa = data.get('placa', '')
        entidad = data.get('entidad', '')

        context = Context({
            "nombre": nombre,
            "placa": placa,
            "entidad": entidad
        })

        template = "Se remite a Sr(a) {{nombre}} la disposición de presentarse en la entidad {{entidad}} con su vehículo de placa {{placa}}."
        template = Template(template)
        generated_text = template.render(context)


        txt_file = io.BytesIO()
        txt_file.write(generated_text.encode('utf-8'))
        txt_file.seek(0)

        # Generate .docx file
        document = Document()
        document.add_paragraph(generated_text)
        docx_file = io.BytesIO()
        document.save(docx_file)
        docx_file.seek(0)


        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            txt_file_name = 'GeneratedFile-{0}.txt'.format(placa)
            docx_file_name = 'GeneratedFile-{0}.docx'.format(placa)
            zip_file.writestr(txt_file_name, txt_file.read())
            zip_file.writestr(docx_file_name, docx_file.read())


        response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment;filename=GeneratedFiles.zip'

        return response
