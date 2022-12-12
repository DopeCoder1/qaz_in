import django
from django.db import models

# Create your models here.
from django.db import models


class CategoryDocuments(models.Model):
    file = models.FileField(upload_to='meeting/documents/category/', verbose_name='Документы по теме')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Документ Категории'
        verbose_name_plural = 'Документы Категории'


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


class OnpfArticles(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    nested_documents = models.ManyToManyField(NestedDocuments, blank=True, verbose_name='Вложенные документы')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='Теги')
    deadline = models.DateTimeField(blank=True, null=True, verbose_name='Срок выполнения')
    executor = models.ForeignKey('Executor', on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='Исполнитель')
    form_realization = models.ForeignKey('FormRealization', on_delete=models.CASCADE, blank=True, null=True,
                                         verbose_name='Форма реализации')
    subcategory3 = models.ForeignKey('Subcategory2', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Executor(models.Model):
    executor_name = models.CharField(max_length=100, verbose_name='Исполнитель')

    def __str__(self):
        return self.executor_name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class FormRealization(models.Model):
    form_name = models.CharField(max_length=100, verbose_name='Форма реализации')

    def __str__(self):
        return self.form_name

    class Meta:
        verbose_name = 'Форма реализации'
        verbose_name_plural = 'Формы реализации'


class SubCategory2(models.Model):
    subcategory_name2= models.CharField(max_length=100, verbose_name='Название Подкатегория 3')
    subcategory2 = models.ManyToManyField('SubCategory', blank=True, verbose_name='Выбор категории 2-уровня')

    def __str__(self):
        return self.subcategory_name2

    class Meta:
        verbose_name = 'Подкатегория 2'
        verbose_name_plural = 'Подкатегории 2'


class SubCategory(models.Model):
    subcategory_name1 = models.CharField(max_length=100, verbose_name='Название Подкатегории 2')
    subcategory1 = models.ManyToManyField('Category', blank=True, verbose_name='Выбор категории 1-уровня')
    def __str__(self):
        return self.subcategory_name1

    class Meta:
        verbose_name = 'Подкатегория 1'
        verbose_name_plural = 'Подкатегории 1'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название категории')
    category_documents = models.ManyToManyField(CategoryDocuments, blank=True, verbose_name='Документы')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
