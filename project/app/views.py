from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.http import Http404

#temporary 
def base(request):
    return render(request, 'base.html')

# Home page
def index(request):
    sliders = Slider.objects.all()
    theaters = MovieTheater.objects.all()
    tvs = MovieTV.objects.all()
    news_items = News.objects.all()
    trailers = TrailerItem.objects.all()

    return render(request, 'index.html', {
        'sliders': sliders,
        'theaters': theaters,
        'tvs': tvs,
        'news_items': news_items,
        'trailers': trailers,
    })


# Movie list page
def movielist(request):
    theaters = MovieTheater.objects.all()
    tvs = MovieTV.objects.all()
    celebs = Celebrity.objects.all()

    return render(request, "movielist.html", {
        "theaters": theaters,
        "tvs": tvs,
        "celebs": celebs,
    })




# Single movie page
def moviesingle(request, id):
    movie = (
        MovieTheater.objects.filter(id=id).first() or
        MovieTV.objects.filter(id=id).first()
    )

    if not movie:
        raise Http404("Movie not found")

    return render(request, 'moviesingle.html', {
        'movie': movie
    })



# News page
def news_list(request):
    news_items = News.objects.all()

    return render(request, 'news.html', {
        'news_items': news_items
    })


# Trailers page
def trailers(request):
    trailer_items = TrailerItem.objects.all()

    return render(request, 'trailers.html', {
        'trailer_items': trailer_items
    })
