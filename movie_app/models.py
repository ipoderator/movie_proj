from django.db import models
from django.urls import reverse 
from django.utils.text import slugify


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    badget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null = False, db_index=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie,self).save(*args, **kwargs)


    def get_url(self):
        return reverse('movie_detail', args=[self.slug])


    def __str__(self) -> str:
        return f'{self.name} - {self.rating}%'
