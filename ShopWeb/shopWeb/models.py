from django.db import models

class Products(models.Model):
    Name= models.CharField(max_length=150)  
    Product_Image=models.ImageField()
    Category= models.CharField(max_length=150)  
    Description=models.TextField()  
    Price=models.CharField(max_length=150)
    def _str_(self):
      return self.id
