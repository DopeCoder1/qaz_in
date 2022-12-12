from django.db import models


# Create your models here.
class CategoryDocuments(models.Model):
    file = models.FileField(upload_to='registry/documents/category/', verbose_name='Документы по теме')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    category_documents = models.ManyToManyField(CategoryDocuments, blank=True, verbose_name='Документы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class NestedDocuments(models.Model):
    file = models.FileField(upload_to='meeting/documents/article/nested/', verbose_name='Документы по теме')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Вложенный документ'
        verbose_name_plural = 'Вложенные документы'


class Links(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название", default='')
    link = models.URLField(verbose_name="Ссылка")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    nested_documents = models.ManyToManyField(NestedDocuments, blank=True, verbose_name='Вложенные документы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
