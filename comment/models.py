from django.db import models

# Create your models here.
from django.db import models
from blog.models import Artikel
from django.contrib.auth.models import User



class Comment(models.Model):
    
    message = models.TextField()
    artikel_creator_username = models.CharField(max_length=200, null=True, blank=True)
    artikel_creator = models.ForeignKey(Artikel, on_delete=models.CASCADE, blank = True, null = True)
    comment_creator = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    created_at = models.CharField(max_length=50,null=True, blank=True)
    comment_creator_username = models.CharField(max_length=200, null=True, blank=True)
    id_forum = models.CharField(max_length=200, null=True, blank=True)
    id_user = models.CharField(max_length=200, null=True, blank=True)
   
