from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

class MeasureUnit(BaseModel):

    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = ("Unidad de medida")
        verbose_name_plural = ("Unidades de medidas")

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):

    description = models.CharField('Descripción', max_length=50, unique=True, null=False, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value


    class Meta:
        verbose_name = ("Categoria del Producto")
        verbose_name_plural = ("Categorias de Productos")

    def __str__(self):
        return self.description

class Indicator(BaseModel):

    descuent_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, verbose_name='Indicador de ofertas', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Indicador de oferta")
        verbose_name_plural = ("Indicadores de ofertas")

    def __str__(self):
        return f'Oferta de la categoria {self.category_product} : {self.descuent_value}' 

class Product(BaseModel):

    name = models.CharField('Nombre de producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción del producto', blank=False, null=False)
    image = models.ImageField('Imagen del producto', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, verbose_name='Unidad de Medida', on_delete=models.CASCADE, null=True)
    category_product = models.ForeignKey(CategoryProduct, verbose_name='Categoria de producto', on_delete=models.CASCADE, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.name