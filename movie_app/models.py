from codecs import backslashreplace_errors
from django.db import models
from django.urls import reverse 
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


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
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    year = models.IntegerField(null=True, blank=True)
    badget = models.IntegerField(default=1000000, blank=True, validators=[
        MinValueValidator(1)
    ])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB) 
    slug = models.SlugField(default='', null = False, db_index=True)


    def get_url(self):
        return reverse('movie_detail', args=[self.slug])


    def __str__(self) -> str:
        return f'{self.name} - {self.rating}%'
