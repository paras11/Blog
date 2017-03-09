from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author =models.CharField(max_length=250)

    title=models.CharField(max_length=250)
    content = models.TextField(default='NO TEXT HERE')
    created_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True , null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

