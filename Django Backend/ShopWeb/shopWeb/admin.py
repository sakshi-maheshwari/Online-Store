from django.contrib import admin
from .models import *
# Register your models here.
class ProductsAdmin(admin.ModelAdmin): 
    list_display = ('Name', 'Product_Image','Category','Description','Price')

Tables = [
    Products
         ]
admin.site.register(Tables)