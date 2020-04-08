from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView  
from .serializers import *
from rest_framework import viewsets
from django.http import HttpResponse
# Create your views here.

class ProductsView(ListCreateAPIView):       
    serializer_class = ProductsSerializer       
    queryset = Products.objects.all()  

def index(request):
    return render(request, 'index.html')
    
def products(request):
    return render(request, 'products.html')