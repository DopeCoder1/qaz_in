from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from free_zone.models import Category, CategoryDocuments, NestedDocuments, FreeZoneArticles, Tags


class ArticlesNote(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)


class CategoryDocumentsAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class NestedDocumentsAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


admin.site.register(NestedDocuments, NestedDocumentsAdmin)
admin.site.register(CategoryDocuments, CategoryDocumentsAdmin)
admin.site.register(Category)
admin.site.register(FreeZoneArticles, ArticlesNote)
admin.site.register(Tags)
