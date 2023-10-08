from django.urls import path
from apps.products.api.views.general_views import MeasuereUnitListAPIView, IndicatorListAPIView, CategoryProductsListAPIView
from apps.products.api.views.products_views import (
    ProductListCreateAPIView, ProductRetrieveAPIView, ProductDestroyAPIView, ProductUpdateAPIView
    )

urlpatterns = [
    #Se crea el nuevo enlace, se llama a la vista
    path('measure_unit/', MeasuereUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    path('category_products/', CategoryProductsListAPIView.as_view(), name='category_products'),
    path('products/', ProductListCreateAPIView.as_view(), name='product_create'),
    path('products/retrieve/<int:pk>', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('products/destroy/<int:pk>', ProductDestroyAPIView.as_view(), name='product_destroy'),
    path('products/update/<int:pk>', ProductUpdateAPIView.as_view(), name='product_update')
]
