from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from tariff.models import Category, CategoryDocuments, NestedDocuments, TariffArticles, Tags


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
admin.site.register(TariffArticles, ArticlesNote)
admin.site.register(Tags)
