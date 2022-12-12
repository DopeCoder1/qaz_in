from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from meeting.models import Category, CategoryDocuments, NestedDocuments, MeetingArticles, Tags


class ArticlesNote(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)


class NestedDocumentsAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class CategoryDocumentsAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


admin.site.register(Category)
admin.site.register(MeetingArticles, ArticlesNote)
admin.site.register(Tags)
admin.site.register(NestedDocuments, NestedDocumentsAdmin)
admin.site.register(CategoryDocuments, CategoryDocumentsAdmin)