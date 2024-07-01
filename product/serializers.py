from rest_framework import serializers
from product.models import  product, Category, ProductVariant, ProductVariantType, vendor, ProductVendor


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
    vendor = serializers.SerializerMethodField()
    class Meta:
        model = product
        fields = '__all__'
       
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor
        fields = '__all__'
        
    