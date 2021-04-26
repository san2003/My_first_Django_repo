from django.db import models
from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug =  models.SlugField(max_length=254, unique=True)
    