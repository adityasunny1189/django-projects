from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index-page'),
	path('posts', views.get_posts, name='posts-page'),
	path('posts/<slug>', views.get_post, name='post-details-page')
]