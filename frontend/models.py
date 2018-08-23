from django.db import models

# Create your models here.
class Settings(models.Model):
    port = models.IntegerField(default=8000)
    batch_size = models.IntegerField(default=5)
    fps = models.IntegerField(default=10)
    ip_address = models.CharField(default='127.0.0.1', max_length=120)
