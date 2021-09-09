from reportlab.lib.colors import magenta, pink, blue
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import pdfkit


def create_pdf():
    options = {'page-size': 'A4', 'dpi': 300}
    pdfkit.from_file('test.html', 'out.pdf', options=options)


def create_simple_checkboxes():
    packet = io.BytesIO()

    c = canvas.Canvas(packet)

    c.setFont("Courier", 20)
    form = c.acroForm

    c.drawString(420, 790, 'N° ')
    form.textfield(name='leTruc', tooltip='numero du truc',
                  x=460, y=780, borderStyle='inset',
                   forceBorder=True)

    c.showPage()
    c.showPage()
    c.showPage()
    c.save()
    packet.seek(0)
    return packet

def merge():

    in_pdf_file = 'out.pdf'
    out_pdf_file = 'with_image.pdf'

    test = create_simple_checkboxes()

    new_pdf = PdfFileReader(test)

    # read the existing PDF
    existing_pdf = PdfFileReader(open(in_pdf_file, "rb"))
    output = PdfFileWriter()

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(i))
        output.addPage(page)

    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()


create_pdf()
merge()