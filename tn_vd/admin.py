from django.contrib import admin
from tn_vd.models import TnVd, SingleCustoms, Country, ImportBans
from import_export.admin import ImportExportMixin


# Register your models here.
class TnVdAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(TnVd, TnVdAdmin)
admin.site.register(SingleCustoms)
admin.site.register(Country)
admin.site.register(ImportBans)
