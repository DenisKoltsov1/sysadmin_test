from django.db import models
from django.urls import reverse



class Blogs(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100,verbose_name='Gmail')
    specialization = models.CharField(max_length=100, verbose_name='Специализация')
    mobile = models.CharField(max_length=100, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    photo = models.ImageField(max_length=100,upload_to='user_photo/')
    
    
  
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('create_blog' )
    
    def get_absolute_url(self):
        return reverse('blogDelete' )
        
 

       