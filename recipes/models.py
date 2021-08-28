from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=30, blank=True)
    image_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    ingredients = models.CharField(max_length=250, blank=True)
    time = models.IntegerField(default=0)

    def __str__(self):
        return self.title
