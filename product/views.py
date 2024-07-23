from product.serializers import ProductSerializer, CategorySerializer, VariantSerializer, VendorSerializer
from rest_framework import viewsets
from product.models import Product, Category, ProductVariant, Vendor
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        category = self.request.query_params.get('Category', None)
        if category:
            queryset = Product.objects.filter(category__category_name=category)
        else:
            queryset = Product.objects.all()
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})
    
    def delete(self, request, pk= None):
        pk = request.data.get('id')
        products = get_object_or_404(Product, pk=pk)
        products.delete()
        return Response({ 'message':'Product deleted successfully'})

class VariantViewSet(viewsets.ModelViewSet):
    serializer_class = VariantSerializer
    queryset = ProductVariant.objects.all()
    
class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    
    

    


    

