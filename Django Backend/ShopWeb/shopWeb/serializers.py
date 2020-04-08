from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields =['Name', 'Product_Image','Category','Description','Price']