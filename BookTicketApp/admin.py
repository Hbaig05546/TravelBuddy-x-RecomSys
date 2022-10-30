''' /BookTicketApp/admin.py '''

from django.contrib import admin
from .models import PackageDetail,TMSBooking

from import_export.admin import ImportExportModelAdmin

@admin.register(PackageDetail)
class PackageDetailAdmin(ImportExportModelAdmin):
    # list_display = ('pLocation','pTitle','pdetails','pic','pCategory','amount')
    pass


# admin.site.register(PackageDetail)
admin.site.register(TMSBooking)