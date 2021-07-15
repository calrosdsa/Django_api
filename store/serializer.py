from .models import Category,Product,ProductImage
from rest_framework import serializers

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields=['image','alt_text']
class ProductSerializer(serializers.ModelSerializer):
    product_image=ProductImageSerializer(many=True,read_only=True)
    class Meta:
        model=Product
        fields=["title","description","category","slug","id","product_image","regular_price"]
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["name","slug"]