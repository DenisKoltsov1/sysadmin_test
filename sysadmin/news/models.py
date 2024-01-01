from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='news', blank=True, null=True)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('create_news' )
    
    def get_absolute_url(self):
        return reverse('delete_news' )
        
    class Meta:
        verbose_name_plural = 'Новости'
        ordering = ['-time_create',]