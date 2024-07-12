from django.contrib import admin
from product.models import Product, Category, ProductVariant, ProductVariantType, Vendor, ProductVendor
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantType)
admin.site.register(Vendor)
admin.site.register(ProductVendor)
