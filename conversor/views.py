from django.shortcuts import render
import os
from django.conf import settings
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render

def converter_txt_pdf(request):
    if request.method == 'POST' and request.FILES.get('arquivo'):
        txt_file = request.FILES['arquivo']
        content = txt_file.read().decode('utf-8')

        buffer = BytesIO()
        c = canvas.Canvas(buffer)

        font_path = os.path.join(settings.BASE_DIR, 'fonts', 'dejavu-fonts-ttf-2.37', 'ttf', 'DejaVuSans.ttf')
        pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))
        c.setFont('DejaVuSans', 12)

        textobject = c.beginText(40, 800)
        for line in content.splitlines():
            textobject.textLine(line)
        c.drawText(textobject)

        c.showPage()
        c.save()

        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="convertido.pdf"'
        return response

    return render(request, 'converter.html')