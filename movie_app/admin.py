from distutils.log import ERROR
from locale import currency
from re import search
from turtle import title
from django.contrib import admin,messages
from .models import Movie, Director
from django.contrib.auth.models import User
from django.db.models import QuerySet 

# Register your models here.

admin.site.register(Director)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name  = 'rating'


    def lookups(self, request: str, model_admin: str) -> str:
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 70', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]


    def queryset(self, request: str, queryset: QuerySet) -> QuerySet:
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'rating', 'badget', 'rating_status','currency']
    list_editable = ['rating','badget','currency']
    list_per_page = 10
    actions = ['set_dollars','set_euro']
    search_fields = ['name', 'rating']
    list_filter = ['name','currency', RatingFilter]


    @admin.display(ordering='rating')
    def rating_status(self,mov: Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть?'
        if mov.rating < 70:
            return 'На разок'
        if mov.rating <= 85:
            return 'Зачет'
        return 'Топчик'
    

    @admin.action(description='Утсановить валюту в долларах')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)


    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EURO)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
        )