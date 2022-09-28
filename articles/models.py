from pyexpat import model
from turtle import title
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models

# Create your models here.

class Article(models.Model):  # 상속
    # id는 자동으로 만들어짐
    title = models.CharField(max_length=10)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
