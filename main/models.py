from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    rating = models.IntegerField(default=0, blank=True, null=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


