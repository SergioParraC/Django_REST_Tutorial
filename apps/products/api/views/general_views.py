from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializer import MeasuereUnitSerializer, IndicatorSerializer, CategoryProductsSerializer
from apps.base.api import GeneralListAPIView
from rest_framework import generics

class MeasuereUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasuereUnitSerializer
    
class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer
    
class CategoryProductsListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductsSerializer