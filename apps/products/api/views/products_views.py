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

"""Mostrar solo un elemento, buscando por el pk enviado por el enlace, se envia por el enlace"""
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

"""Eliminar un producto, se envia por el enlace"""
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    """Se modifica el metodo eliminar para que en teoria no elimine de la base de datos"""
    def delete(self, request, pk=None):
        #Busca el elemento desde el pk enviado por el url
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            #Unicamente se cambia el estado para que no aparezca en la vista, los elementos no se deben eliminar
            product.save()
            #Si se puede eliminar, retorna un mensaje de que ha funcionado
            return Response({'message': 'Producto eliminado correctamente'}, status = status.HTTP_200_OK)
        #Si no, muestra un error
        return Response({'error': 'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self, pk):
        #Para no repetir consultas, se hace todo el query en la siguiente linea
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id=pk).first()
    
    def patch(self, request, pk=None):
        #Se llama la información que está en la base de datos
        if self.get_queryset(pk):
            #Se pasa la solicitud al serializer
            product_serializer=self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        #Se envia la pk para que la consulte
        if self.get_queryset(pk):
            #Se mandan dos parametros, el inicial y el request con los cambios
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)