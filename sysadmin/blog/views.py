
from .forms import BlogForm
from .models import Blogs

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin



from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView







import requests

class Blog(ListView):
    model = Blogs
    
    template_name ='blog.html'
    queryset  = Blogs.objects.all()

class BlogDeletes(UserPassesTestMixin,DeleteView):
    model=Blogs   
    success_url='/'
    template_name= 'blog_delete.html'
    def test_func(self):
        return self.request.user.is_staff
    
class BlogCreate(UserPassesTestMixin,CreateView):
    model = Blogs
    form_class = BlogForm
    success_url = '/'
    template_name = 'blog_form.html'

    def test_func(self):
        return self.request.user.is_staff


 
    

    
