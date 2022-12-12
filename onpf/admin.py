from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportMixin

from onpf.models import Category, CategoryDocuments, NestedDocuments, SubCategory, OnpfArticles, Tags, FormRealization, \
    Executor, SubCategory2


class ArticlesNote(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)


class NestedDocumentsAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class CategoryDocumentsAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


admin.site.register(Category)
admin.site.register(CategoryDocuments, CategoryDocumentsAdmin)
admin.site.register(NestedDocuments, NestedDocumentsAdmin)
admin.site.register(OnpfArticles, ArticlesNote)
admin.site.register(Tags)
admin.site.register(SubCategory)
admin.site.register(FormRealization)
admin.site.register(Executor)
admin.site.register(SubCategory2)
