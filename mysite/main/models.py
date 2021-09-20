from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    
    def get_absolute_url(self):
        return reverse('company_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    slug = models.SlugField(unique=True)
    
    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.name

class Sample(models.Model):
    sample = models.SlugField(unique=True)
    date_pub = models.DateField(auto_now_add=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    categorys = models.ManyToManyField('Category', blank=True,related_name='samples')

    def __str__(self):
        return self.sample

    def get_absolute_url(self):
        return reverse('sample_detail_url', kwargs={'sample': self.sample})