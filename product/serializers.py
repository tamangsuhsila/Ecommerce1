from rest_framework import serializers
from product.models import  Product, Category, ProductVariant,Vendor


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    variant_type = VariantSerializer()
    # vendor = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
       
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        
    