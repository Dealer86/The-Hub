from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=400, default="Unknown Title")
    image = models.URLField(default="No image")
    date = models.CharField(max_length=100, default="Unknown Date")
    address = models.CharField(max_length=200, default="Unknown Address")
    link = models.URLField(default="Unknown Link")
    description = models.CharField(max_length=300, default="Description not available")

    def __str__(self):
        return self.title
