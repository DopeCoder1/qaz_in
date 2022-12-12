from django.db import models

# Create your models here.
from django.db import models


class CategoryDocuments(models.Model):
    file = models.FileField(upload_to='meeting/documents/category/', verbose_name='Документы по теме')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class NestedDocuments(models.Model):
    file = models.FileField(upload_to='meeting/documents/article/nested/', verbose_name='Документы по теме')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Вложенный документ'
        verbose_name_plural = 'Вложенные документы'


class Tags(models.Model):
    name = models.CharField(max_length=100, verbose_name='Теги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class FreeZoneArticles(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    nested_documents = models.ManyToManyField(NestedDocuments, blank=True, verbose_name='Вложенные документы')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='Теги')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название категории')
    category_documents = models.ManyToManyField(CategoryDocuments, blank=True, verbose_name='Документы')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
