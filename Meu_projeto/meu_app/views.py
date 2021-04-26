from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post
# Create your views here.

class PostListView(Listview):
    model = Post

class PostDetailView(Detailview):
    model = Post