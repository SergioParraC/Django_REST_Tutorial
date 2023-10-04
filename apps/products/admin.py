from django.contrib import admin
from apps.products.models import *

# Register your models here.

class MeasuereUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(MeasureUnit, MeasuereUnitAdmin)
admin.site.register(CategoryProduct, CategoryAdmin)
admin.site.register(Indicator)
admin.site.register(Product)