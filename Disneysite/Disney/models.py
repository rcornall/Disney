from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    poster = models.ImageField()
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=4)


    def __str__(self):
        return self.title + ", " + self.year + "img: " + self.poster

