from django.db import models
from datetime import date, datetime
from authors.models import Author



class Categories(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=date.today())
    time = models.TimeField(default=datetime.now().strftime("%H:%M:%S"))
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

