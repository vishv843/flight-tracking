from django.db import models

# Create your models here.
class event(models.Model):
    airline = models.CharField(max_length = 30)