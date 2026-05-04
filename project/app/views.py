from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import (
    Slider,
    Movie,
    News,
    TrailerItem,
    Celebrity
)


# BASE (TEMP)
def base(request):
    return render(request, 'base.html')


# HOME PAGE
def index(request):
    sliders = Slider.objects.all()

    # FIX: split for template expectations
    theaters = Movie.objects.filter(type="theater")
    tvs = Movie.objects.filter(type="tv")

    news_items = News.objects.all()
    trailers = TrailerItem.objects.all()
    celebs = Celebrity.objects.all()

    print("THEATERS:", theaters)
    print("TVS:", tvs)

    return render(request, 'index.html', {
        'sliders': sliders,

        # IMPORTANT: match template names
        'popular_theaters': theaters,
        'coming_theaters': theaters,

        'popular_tvs': tvs,
        'coming_tvs': tvs,

        'news_items': news_items,
        'trailers': trailers,
        'celebs': celebs,
    })


# MOVIE LIST PAGE
def movielist(request):
    theaters = Movie.objects.filter(type="theater")
    tvs = Movie.objects.filter(type="tv")
    celebs = Celebrity.objects.all()

    return render(request, "movielist.html", {
        # FIX: match template variables
        "popular_theaters": theaters,
        "coming_theaters": theaters,

        "popular_tvs": tvs,
        "coming_tvs": tvs,

        "celebs": celebs,
    })


# SINGLE MOVIE PAGE
def moviesingle(request, id):
    movie = get_object_or_404(Movie, id=id)

    return render(request, 'moviesingle.html', {
        'movie': movie
    })


# NEWS PAGE
def news_list(request):
    news_items = News.objects.all()

    return render(request, 'news.html', {
        'news_items': news_items
    })


# TRAILERS PAGE
def trailers_view(request):
    trailers_list = TrailerItem.objects.all()

    return render(request, 'trailers.html', {
        'trailers': trailers_list
    })