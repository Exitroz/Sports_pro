from django.db import models
from django.conf import settings
from .utils import generate_slug

# Create your models here.



class BlogPostModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blogPost/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogPostModel, self).save(*args, **kwargs)
    
   
    def get_image_url(self):
        image_url = self.image.url
        return image_url

    
