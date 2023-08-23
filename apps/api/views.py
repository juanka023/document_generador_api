import io
import zipfile
from docx import Document
from django.http import HttpResponse
from django.template import Context, Template
from rest_framework.views import APIView

class DocumentGenerationView(APIView):
    def post(self, request):
        data = request.data
        input_file = data.get('input_file', None)
        txt_template = "Se remite a Sr(a) {{nombre}} la disposición de presentarse en la entidad {{entidad}} con su vehículo de placa {{placa}}."


        if input_file:
            # Read content of the uploaded file
            content = input_file.read().decode('utf-8')

            if input_file.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                # If it's a DOCX, generate text from template
                txt_template = Template(txt_template)
                context = {}
                for line in content.splitlines():
                    key, value = line.split(':', 1)
                    context[key.strip()] = value.strip()

            else:
                # Assuming plain text input
                context = {}
                for line in content.splitlines():
                    key, value = line.split(':', 1)
                    context[key.strip()] = value.strip()
                txt_template = Template(txt_template)

        else:
            # Use data directly from JSON
            context = {
                "nombre": data.get('nombre', ''),
                "placa": data.get('placa', ''),
                "entidad": data.get('entidad', ''),
            }

            # Generate .txt file
            txt_template = Template(txt_template)

        # Generate .txt file
        generated_text = txt_template.render(Context(context))
        txt_file = io.BytesIO()
        txt_file.write(generated_text.encode('utf-8'))
        txt_file.seek(0)

        # Generate .docx file
        docx_template = Document()
        docx_template.add_paragraph(generated_text)
        docx_file = io.BytesIO()
        docx_template.save(docx_file)
        docx_file.seek(0)

        # Create a ZIP file containing both files
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr('GeneratedFile.txt', txt_file.getvalue())
            zip_file.writestr('GeneratedFile.docx', docx_file.getvalue())

        # Prepare response for the ZIP file
        response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment;filename=GeneratedFiles.zip'

        return response
