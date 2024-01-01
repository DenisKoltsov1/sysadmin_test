from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from news.views import NewsList,CreateNews,UpdateNews,NewsDelete,NewsDetailView
from news.models import News
urlpatterns = [  
    
    path('', NewsList.as_view(), name='news'), 
    path('news-create/', CreateNews.as_view(), name='news_create'),
    path('news-update/<int:pk>', UpdateNews.as_view(), name='news_update'),
    path('news-delete/<int:pk>', NewsDelete.as_view(), name='news_delete'),
    path('news-detail/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
   
   ]

