from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializer import MeasuereUnitSerializer, IndicatorSerializer, CategoryProductsSerializer
from rest_framework import generics

class MeasuereUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasuereUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state = True)
    
class IndicatorListAPIView(generics.ListAPIView):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return Indicator.objects.filter(state = True)
    
class CategoryProductsListAPIView(generics.ListAPIView):
    serializer_class = CategoryProductsSerializer

    def get_queryset(self):
        return CategoryProduct.objects.filter(state = True)