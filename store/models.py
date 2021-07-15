from django.db import models
from django.db.models.fields import BooleanField
from mptt.models import MPTTModel,TreeForeignKey
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Category(MPTTModel):
    name=models.CharField(verbose_name=_("name"),help_text=_("This field is required"),max_length=255,unique=True)
    slug=models.SlugField(verbose_name=_("Safe url"),max_length=255,unique=True)
    parent=TreeForeignKey("self",on_delete=models.CASCADE, null=True, blank=True ,related_name="children")
    is_active=models.BooleanField(default=True)

    class MPPTMeta:
        order_insetion_by=["name"]
    class Meta:
        verbose_name=_("Category")
        verbose_name_plural=_("Categories")
    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    def __str__(self):
        return self.name

class ProductType(models.Model):
    name=models.CharField(verbose_name=_("Type"),help_text=_("is querired"),max_length=255,unique=True)
    is_active=models.BooleanField(default=True)
    class Meta:
        verbose_name=_("Product Type")
        verbose_name_plural=_("Product Types")

    def __str__(self):
        return self.name
class ProductSpecification(models.Model):
    product_type=models.ForeignKey(ProductType,on_delete=models.RESTRICT)
    name=models.CharField(verbose_name=_("Nombre"),help_text=_("This field requerid"),max_length=255)

    class Meta:
        verbose_name=_("Product Specification")
        verbose_name_plural=_("Especificaciones del producto")
    def __str__(self):
        return self.name

class Product(models.Model):
    product_type=models.ForeignKey(ProductType,on_delete=models.RESTRICT)
    category=models.ForeignKey(Category,on_delete=models.RESTRICT)
    title=models.CharField(verbose_name=_("Title"),help_text=_("Is required"),max_length=255)
    description=models.TextField(verbose_name=_("Description"),help_text=_("No requerido"),blank=True)
    slug=models.SlugField(max_length=255)
    is_active=models.BooleanField(default=True)
    regular_price=models.DecimalField(verbose_name=_("Regular Precio"),help_text=_("Max 99999"),error_messages={
        "name":{
            "max_length":_("The price must be between 0 and 999999")
        },
    },max_digits=8,decimal_places=2)
    discount_price=models.DecimalField(verbose_name=_("Discount Price"),help_text=_("Max 99999"),error_messages={
        "name":{
            "max_length":_("The discout must be between 0 and 99999")
        },
    },decimal_places=2,max_digits=8)
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=("-created_at",)
        verbose_name=_("Product")
        verbose_name_plural=_("Products")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])
class ProductSpecificationValue(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    specification=models.ForeignKey(ProductSpecification,on_delete=models.CASCADE,related_name="specifications")
    value=models.CharField(verbose_name=_("value"),help_text=_("Product Specification Value max 255words"),max_length=255)
    class Meta:
        verbose_name=_("Product Specification Value")
        verbose_name_plural=_("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image")
    image=models.ImageField(verbose_name=_("Image"),help_text=_("Upload a product Image"),upload_to="images/",default="images/default.png")
    alt_text=models.CharField(verbose_name=_("Texto alternativo"),help_text=_("Please add a alternative text"),
    blank=True,null=True,max_length=255)
    is_feature=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name=_("Product Image")
        verbose_name_plural=_("Product Images")