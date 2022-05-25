from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    your_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'your_discount'
        ]
        
    def get_your_discount(self, obj):
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        # if not hasattr(obj, 'id'):
        #     return None
        # if not isinstance(obj, Product):
        #     return None
        return obj.get_discount()