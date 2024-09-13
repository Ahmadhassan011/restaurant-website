from django.db import models
import datetime
from PIL import Image

# Create your models here.

class home_images(models.Model):
    image = models.ImageField(upload_to='home_images/')
    welcome_01 = models.CharField(max_length=30)
    welcome_02 = models.CharField(max_length=30)
    description = models.TextField(default='Our Restaurant')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.welcome_01

class Appetizers(models.Model):
    image = models.ImageField(upload_to='menu/appetizer/', default='default_image.jpg')
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(default='Our Appetizers')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Main_course(models.Model):
    image = models.ImageField(upload_to='menu/main_course/', default='default_image.jpg')
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(default='Our Main Course')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Dessert(models.Model):
    image = models.ImageField(upload_to='menu/dessert/', default='default_image.jpg')
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(default='Our Desserts')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Chef(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Our Chef')
    image = models.ImageField(upload_to='chefs/', default='default_image.jpg')
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} : {self.message}"