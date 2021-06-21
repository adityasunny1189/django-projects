from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from .models import Post


def get_date(post):
	return post['date']


# Create your views here.
def index(request):
	latest_posts = Post.objects.all().order_by('-date')[:3]
	return render(request, 'my_blog/index.html', {
			"posts": latest_posts
		})


def get_posts(request):
	posts = Post.objects.all().order_by('-date')
	return render(request, 'my_blog/posts.html', {
			"posts": posts
		})


def get_post(request, slug):
	post = Post.objects.get(slug=slug)
	return render(request, 'my_blog/post-detail.html', {
			"post": post 
		}) 

