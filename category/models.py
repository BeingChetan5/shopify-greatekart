from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=20, unique=True)  # Slug is nothing but URL of category
    description = models.TextField(max_length=255)
    category_image = models.ImageField(upload_to='photos/categories/', blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    

