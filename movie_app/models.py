from django.db import models
from django.urls import reverse 


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    badget = models.IntegerField(default=1000000)


    def get_url(self):
        return reverse('movie_detail', args=[self.id])


    def __str__(self) -> str:
        return f'{self.name} - {self.rating}%'
