from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, default="Unknown Title")
    date = models.CharField(max_length=100, default="Unknown Date")
    address = models.CharField(max_length=200, default="Unknown Address")
    link = models.URLField(default="Unknown Link")

    def __str__(self):
        return self.title
