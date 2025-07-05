import os
from io import BytesIO
import tempfile
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings
import fitz  # PyMuPDF para ler PDF
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from docx import Document
from pdf2docx import Converter

def converter(request):
    if request.method == 'POST' and request.FILES.get('arquivo'):
        arquivo = request.FILES['arquivo']
        tipo_conversao = request.POST.get('conversao')
        nome = arquivo.name.lower()

        # Caminho absoluto da fonte TTF
        font_path = os.path.join(settings.BASE_DIR, 'fonts', 'dejavu-fonts-ttf-2.37', 'ttf', 'DejaVuSans.ttf')

        if tipo_conversao == 'txt-pdf' and nome.endswith('.txt'):
            content = arquivo.read().decode('utf-8')
            buffer = BytesIO()
            c = canvas.Canvas(buffer)
            pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))
            c.setFont('DejaVuSans', 12)
            textobject = c.beginText(40, 800)
            for line in content.splitlines():
                textobject.textLine(line)
            c.drawText(textobject)
            c.showPage()
            c.save()
            buffer.seek(0)
            return HttpResponse(buffer, content_type='application/pdf', headers={
                'Content-Disposition': 'attachment; filename="convertido.pdf"'
            })

        elif tipo_conversao == 'pdf-txt' and nome.endswith('.pdf'):
            buffer = BytesIO(arquivo.read())
            texto = ''
            with fitz.open(stream=buffer, filetype="pdf") as pdf:
                for page in pdf:
                    texto += page.get_text()
            return HttpResponse(texto, content_type='text/plain; charset=utf-8', headers={
                'Content-Disposition': 'attachment; filename="convertido.txt"'
            })

        elif tipo_conversao == 'docx-pdf' and nome.endswith('.docx'):
            docx_bytes = arquivo.read()
            doc = Document(BytesIO(docx_bytes))
            buffer = BytesIO()
            c = canvas.Canvas(buffer)
            pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))
            c.setFont('DejaVuSans', 12)
            textobject = c.beginText(40, 800)
            for para in doc.paragraphs:
                textobject.textLine(para.text)
            c.drawText(textobject)
            c.showPage()
            c.save()
            buffer.seek(0)
            return HttpResponse(buffer, content_type='application/pdf', headers={
                'Content-Disposition': 'attachment; filename="convertido.pdf"'
            })

        elif tipo_conversao == 'pdf-docx' and nome.endswith('.pdf'):
            pdf_bytes = arquivo.read()
            with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp_pdf:
                tmp_pdf.write(pdf_bytes)
                tmp_pdf.flush()  # garante escrita no disco

                converter = Converter(tmp_pdf.name)
                buffer_docx = BytesIO()
                converter.convert(buffer_docx)
                converter.close()
                buffer_docx.seek(0)
                return FileResponse(buffer_docx, as_attachment=True, filename='convertido.docx')

        else:
            return HttpResponse("Formato ou tipo de conversão inválido. Verifique seu arquivo e a opção selecionada.")

    return render(request, 'converter.html')


def about(request):
    return render(request, 'about.html')