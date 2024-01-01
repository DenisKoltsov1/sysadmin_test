from django.db import models
from django.urls import reverse

class Price(models.Model):
    title = models.CharField(max_length=255);
    content = models.TextField(blank=True)
    price = models.IntegerField()



    def __str__(self):
        return self.title,self.content,self.price


    class Meta:
        verbose_name_plural = 'Цены'