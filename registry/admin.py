from django.contrib import admin
from registry.models import Category, Links, CategoryDocuments, NestedDocuments


# Register your models here.

class CategoryDocumentsAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class NestedDocumentsAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


admin.site.register(CategoryDocuments, CategoryDocumentsAdmin)
admin.site.register(NestedDocuments, NestedDocumentsAdmin)
admin.site.register(Category)
admin.site.register(Links)
