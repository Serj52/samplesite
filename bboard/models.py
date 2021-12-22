from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=20, verbose_name='Haзвaниe')

class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')




    # Create your models here.
