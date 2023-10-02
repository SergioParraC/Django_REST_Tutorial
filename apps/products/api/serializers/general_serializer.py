from apps.products.models import MeasureUnit, CategoryProduct, Indicator
from rest_framework import serializers

class MeasuereUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        #De todos los campos que tiene, este no lo va a retornar en la consulta
        exclude = ('state', 'create_date', 'modified_date', 'delete_day')

class CategoryProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        exclude = ('state', 'create_date', 'modified_date', 'delete_day')

class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ('state', 'create_date', 'modified_date', 'delete_day')