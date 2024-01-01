from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
class Head(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Заголовок')
    content = models.CharField(max_length=1000000000, blank=False, verbose_name='Контент')
#    photo = models.ImageField(max_length=100,blank=True,upload_to='user_photo/')
#    photo1 = models.ImageField(max_length=100,blank=True, upload_to='user_photo/')
#    photo2 = models.ImageField(max_length=100, blank=True ,upload_to='user_photo/')



    class Meta:
        verbose_name = 'Главная'
        #verbose_name_plural = 'Пользователи'


    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.title,self.content )

#,self.photo,self.photo1,self.photo2
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name_plural = 'Главная'