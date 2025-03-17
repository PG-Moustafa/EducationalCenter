from django.contrib import admin
from .models import Student

admin.site.register(Student)

from django.urls import path
from django.utils.html import format_html
from django.urls import reverse

##
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'download_certificate')

    def download_certificate(self, obj):
        return format_html(
            '<a class="button" href="{}">Download PDF</a>',
            reverse('generate_certificate_pdf', args=[obj.id])
        )
    download_certificate.short_description = 'Certificate'
    download_certificate.allow_tags = True
