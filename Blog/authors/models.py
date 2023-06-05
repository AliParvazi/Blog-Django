from django.db import models
from datetime import datetime
class Author(models.Model):
    username = models.CharField(max_length=200)
    rank = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    joined_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.username
        