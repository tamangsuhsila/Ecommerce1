from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
       self.slug = slugify(self.category_name)
       super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name
    
class ProductVariantType(models.Model):
    variant_type = models.CharField(max_length=100)
    variant_name = models.ForeignKey('ProductVariant', on_delete=models.PROTECT)

    def __str__(self):
        return self.variant_type

class ProductVariant(models.Model):
    variant_name = models.CharField(max_length=100)

    def __str__(self):
        return self.variant_name

class product(models.Model):
    product_name=models.CharField(max_length=100)
    description=models.TextField()
    stock=models.IntegerField(default=100)
    price=models.DecimalField(default=0, decimal_places=2, max_digits=1000)
    
    image=models.ImageField(upload_to='static/product',blank=True)

    # season= models.CharField(max_length=100, choices=(('winter','W'),
    #                                                   ('summer','S'),
    #                                                   ('monsoon','M')))
    # gender = models.CharField(max_length=100, choices=(('male','M'),
    #                                                    ('female','F')))
    variant_type = models.ForeignKey(ProductVariantType, on_delete=models.PROTECT)
    
    discount = models.IntegerField()
    
    def __str__(self):
        return self.product_name
    
class vendor(models.Model):
    vendor_name=models.CharField(max_length=100)
    vendor_address=models.TextField()
    vendor_email=models.EmailField()
    vendor_phone=models.IntegerField()
    
    def __str__(self):
        return self.vendor_name
    
class ProductVendor(models.Model):
    product = models.ForeignKey('product', on_delete=models.PROTECT)
    vendor = models.ForeignKey('vendor', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.product.product_name + ' - ' + self.vendor.vendor_name
    
