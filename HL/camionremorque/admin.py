from django.contrib import admin
from .models import Camion,Remorque
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class FilterCamion(admin.ModelAdmin):
    list_display = ("id",
                    "matriculation",
                    "designation",
                    "remorque",
                    )

class FilterRemorque(admin.ModelAdmin):
    list_display = ("id",
                    "matriculation",
                    
                    )

# admin.site.register(Camion, FilterCamion)
@admin.register(Camion)
class CamionImportExport(ImportExportModelAdmin):
    pass
@admin.register(Remorque)
class RemorqueImportExport(ImportExportModelAdmin):
    pass

# admin.site.register(Remorque, FilterRemorque)