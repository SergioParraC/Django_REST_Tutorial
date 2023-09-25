from django.db import models

"""Modelo base para crear los otros modelos"""
class BaseModel(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado',default = True)
    create_date = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de modificación', auto_now=True, auto_now_add=False)
    delete_day = models.DateField('Fecha de eliminación', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = ("Modelo base")
        verbose_name_plural = ("BaseModels")
