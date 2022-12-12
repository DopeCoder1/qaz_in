from django.db import models


# Create your models here.
class TnVd(models.Model):
    code = models.CharField(max_length=100, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ТН ВД'
        verbose_name_plural = 'ТН ВД'


class SingleCustoms(models.Model):
    code = models.ForeignKey(TnVd, on_delete=models.CASCADE, verbose_name='Код')
    import_rate = models.IntegerField(verbose_name='Ставка ввозной таможенной пошлины')
    ETT = models.CharField(max_length=100, verbose_name='Ед. таможенной тарификации')
    income = models.CharField(max_length=100, verbose_name='Доходы')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Единая таможенная пошлина'
        verbose_name_plural = 'Единая таможенные пошлины'


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Страна')
    npa = models.CharField(max_length=100, verbose_name='НПА')
    deadline = models.DateTimeField(verbose_name='Срок')
    deadline2 = models.DateTimeField(verbose_name='Срок2')
    supplies = models.CharField(max_length=100, verbose_name='Поставки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class ImportBans(models.Model):
    code = models.ForeignKey(TnVd, on_delete=models.CASCADE, verbose_name='Код')
    ban = models.CharField(max_length=100, verbose_name='Запреты')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Запрет'
        verbose_name_plural = 'Запреты'
