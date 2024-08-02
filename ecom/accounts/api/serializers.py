from rest_framework import serializers
from Product.models import Product,Variation,Image
from rest_framework import serializers





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 



