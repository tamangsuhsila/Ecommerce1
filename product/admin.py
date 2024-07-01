from django.contrib import admin
from product.models import product, Category, ProductVariant, ProductVariantType, vendor, ProductVendor
# Register your models here.

admin.site.register(product)
admin.site.register(Category)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantType)
admin.site.register(vendor)
admin.site.register(ProductVendor)
