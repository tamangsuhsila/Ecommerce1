from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, CategoryViewSet, VariantViewSet, VendorViewSet



router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'variant', VariantViewSet)
router.register(r'vendor', VendorViewSet)

urlpatterns = [
    path('', include(router.urls))   
]

