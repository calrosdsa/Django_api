from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from mptt import register
from  mptt.admin import MPTTModelAdmin
from .models import (Category,Product,ProductImage,ProductSpecification,ProductSpecificationValue,ProductType)

admin.site.register(Category,MPTTModelAdmin)

class ProductSpecificationInLine(admin.TabularInline):
    model=ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines=[ProductSpecificationInLine,]

class ProductImageInLine(admin.TabularInline):
    model=ProductImage

class ProductSpecificationValueInLine(admin.TabularInline):
    model=ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[
    ProductSpecificationValueInLine,
    ProductImageInLine,
    ]
    