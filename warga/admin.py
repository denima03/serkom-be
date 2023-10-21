from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Warga


@admin.register(Warga)
class WargaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nik', 'nama', 'jenis_kelamin', 'alamat', 'rt', 'rw')
    list_filter = ('jenis_kelamin', 'rt')
    search_fields = ['nama', 'rt', 'rw']
    list_per_page = 10
