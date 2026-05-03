from django.urls import path
from app import views

#this is where the routing occurs
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movielist, name='movielist'),
    path('moviesingle/<int:id>/', views.moviesingle, name='moviesingle'),
    path('news/', views.news_list, name='news'),
    path('trailers/', views.trailers, name='trailers'),
]