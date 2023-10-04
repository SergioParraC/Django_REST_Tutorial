from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializer import ProductSerializers
from rest_framework import generics, status
from rest_framework.response import Response

class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializers

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializers

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto agregado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)