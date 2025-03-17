from django.http import HttpResponse
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Student  # Replace with your user model

def generate_certificate_pdf(request, user_id):
    # Fetch the user or student object
    user = Student.objects.get(id=user_id)  # Replace with your user model

    # Create a BytesIO buffer to store the PDF
    buffer = BytesIO()

    # Create the PDF object using the buffer
    pdf = canvas.Canvas(buffer)

    # Add content to the PDF
    pdf.drawString(100, 750, "Certificate of Completion")
    pdf.drawString(100, 730, f"This certificate is awarded to:")
    pdf.drawString(100, 710, f"{user.first_name} {user.last_name}")
    pdf.drawString(100, 690, "For successfully completing the course.")
    pdf.drawString(100, 670, f"Date: {user.enrollment_date}")  # Example field

    # Save the PDF
    pdf.showPage()
    pdf.save()

    # Get the value of the buffer and create an HTTP response
    pdf_data = buffer.getvalue()
    buffer.close()

    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{user.id}.pdf"'
    return response