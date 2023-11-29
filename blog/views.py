from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import  ListView
from .models import Post

# Create your views here.
class BlogPageView(TemplateView):
    template_name="blog.html"


