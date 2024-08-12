from django.db import models

class Project(models.Model):
    movieName = models.CharField(max_length= 30)
    releaseDate = models.DateField()
    rating = models.FloatField()

# Create your models here.
