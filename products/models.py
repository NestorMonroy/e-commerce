from django.db import models
from django.db.models.signals import pre_save, post_save
import random
import os
from django.urls import reverse

from .utils import unique_slug_generator

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
    

def upload_image_path(instace, filename):
  new_filename = random.randint(1, 100)
  name, ext = get_filename_ext(filename)
  final_filename = f'{new_filename}{ext}'
  return f'products/{new_filename}/{final_filename}' 



class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def features(self):
        return self.get_queryset().featured()
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)



    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
      return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product) 