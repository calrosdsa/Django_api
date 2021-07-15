from store.serializer import ProductSerializer
from django.shortcuts import render
from .models import Category, Product
from . import models
from rest_framework import generics
from .serializer import CategorySerializer, ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class Product(generics.RetrieveAPIView):
    lookup_field="slug"
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class CategoryItemView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.filter(
            category__in=Category.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )

class CategoryListView(generics.ListAPIView):
    queryset=Category.objects.filter(level=1)
    serializer_class=CategorySerializer
    

