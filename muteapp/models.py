from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=64)
    phone=models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    category_name= models.CharField(max_length=200,default=1)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name=models.CharField(max_length=64)
    category  = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.product_name

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    price=models.CharField(max_length=100)
    email = models.EmailField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    