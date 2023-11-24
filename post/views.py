from django.shortcuts import render
from .models import Post, Media

# Create your views here.
def post(request):
    posts = Post.objects.all()
    return render(request=request, template_name='index.html', context={'posts':posts})

def details(request, pk):
    post = Post.objects.get(id = pk)
    img = Media.objects.filter(post = pk)
    return render(request=request, template_name='post.html', context={'post':post, 'img':img})