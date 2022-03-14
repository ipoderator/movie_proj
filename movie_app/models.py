from django.db import models
from django.urls import reverse 
from django.utils.text import slugify


class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]


    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    badget = models.IntegerField(default=1000000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB) 
    slug = models.SlugField(default='', null = False, db_index=True)


    def get_url(self):
        return reverse('movie_detail', args=[self.slug])


    def __str__(self) -> str:
        return f'{self.name} - {self.rating}%'
