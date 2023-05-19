from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Images')

class Service(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Images')
    name = models.CharField(max_length=50)

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField()

class Task(models.Model):
    name = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/category")
    not_available = models.BooleanField(default= False)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    

