from django.db import models


class NewsArticle(models.Model):
    author = models.CharField(max_length=255, default="Unknown author")
    title = models.CharField(max_length=255, default="Unknown title")
    url = models.URLField(default="Unknown URL")

    def __str__(self):
        return self.title
