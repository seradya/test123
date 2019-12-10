from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(verbose_name = 'Улица', null = False, blank = False, max_length=64)
    house = models.CharField(verbose_name = 'Дом', null = False, blank = False, max_length=16)
    flat = models.PositiveSmallIntegerField(verbose_name = 'Квартира', null = False, blank = False, max_length=5)
