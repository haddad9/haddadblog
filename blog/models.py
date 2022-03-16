from django.db import models

# Create your models here.
from django.db import models


class Artikel(models.Model):
    title = models.TextField()
    message = models.TextField()
    created_at = models.CharField(max_length=50)
    username = models.TextField(null=True)
    
   