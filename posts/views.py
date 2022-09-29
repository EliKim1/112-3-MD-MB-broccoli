from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy('list')

class PostUpdateView(UpdateView):
    template_name = "posts/update.html"
    model = Post
    fields = ["title", "subtitle", "body"]






