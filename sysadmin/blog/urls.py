from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from blog.views import BlogDeletes,BlogCreate,Blog
urlpatterns = [
   
    path('', Blog.as_view(), name='blog'),
    path('blog-create/',BlogCreate.as_view()),
    path('blogDelete/<int:pk>', BlogDeletes.as_view(),name='blogDelete'),
  
   ]


