from django.db import models

class cards(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    img = models.ImageField(upload_to="ecommerce/img", null=True, blank=True)

class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    img = models.ImageField(upload_to="shop/Category", null=True, blank=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    price= models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/Product", null=True, blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name