from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, "post_list.html", {"posts":posts})

class PostView(ListView):
    template_name = "post_list.html"
    model = Post