from apps.products.models import Product
from apps.products.api.serializers.general_serializer import MeasuereUnitSerializer, CategoryProductsSerializer, IndicatorSerializer
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):
    
    """
    METODO 1:
    Para realizar las relaciones, es decir, que no se muestre los id's de las relaciones, si no los elementos como
    tal. se puede usar los seralizadores que ya se tienen creados
    NOTA: Se debe poner el nombre de la variable tal cual esta en el modelo, Dajngo identifica el modelo de esta
    manera para enviar los datos a la vista}

    measure_unit = MeasuereUnitSerializer()
    category_product = CategoryProductsSerializer()
    """
    
    """
    METODO 2:
    Se utiliza el metodo __str__ modificado del modelo para mostrar la información, se tiene que poner en el nombre
    de la variable el mismo del modelo, si no, no realiza la busqueda

    measure_unit = serializers.StringRelatedField()
    category_product = serializers.StringRelatedField()
    """

    """
    METODO 3:
    Se reescribe el metodo to_representation para dar la información requerida, igualmente se tiene que citar
    las dependencias por el nombre del modelo, para adquirir esta información. Se puede personalizar campo 
    por campo, lo cual da mayor flexibilidad en la información faltante o para mostrar cierta información
    """

    class Meta:
        model = Product
        exclude = ('state', 'create_date', 'modified_date', 'delete_day')

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            #Se revisa si existe alguna imagen, si no esta entonces envia caranteres vacios y no un error
            'image': instance.image if instance.image else None,
            'measure_unit': {
                #'id': instance.measure_unit.id if instance.measure_unit.id is not None else '',
                'description': instance.measure_unit.description if instance.measure_unit is not None else ''
            },
            'category_product': instance.category_product.description if instance.category_product is not None else ''
        }