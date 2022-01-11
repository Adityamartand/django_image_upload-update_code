from django.db import models


# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=10, default=0)
    image = models.ImageField(upload_to="media/",max_length=254, blank=True)

    def __str__(self):
        return self.name
