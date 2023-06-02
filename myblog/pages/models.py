from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, default="unsorted")
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

    def save(self, *args, **kwargs):
        self.name = self.name.lower().replace('-', ' ')
        return super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="New Post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)


    def __str__(self):
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    
