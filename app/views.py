from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app.models import Title, StreamingPlatform

def default(request):
    template = loader.get_template('index.html')

    context = {}

    # get all movie platform
    platforms = StreamingPlatform.objects.all()
    context.update({"platforms":platforms})
    context.update({"movie_types":Title.TYPE_CHOICES})

    # get rating 
    ratings = []
    for t in Title.objects.values('rating').distinct():
        ratings.append(t['rating'])
    context.update({"ratings":sorted(ratings)})
    
    filter_query = {}

    title = request.GET.get("title")
    if title:
        filter_query.update({"title__contains":title})
    platform = request.GET.get("platform")
    if platform:
        filter_query.update({"platform":platform})
    type = request.GET.get("type")
    if type:
        filter_query.update({"type":type})
    rating = request.GET.get("rating")
    if rating:
        filter_query.update({"rating":rating})
    if filter_query:
        movies = Title.objects.filter(**filter_query)
        context.update({"movies":movies})

    return HttpResponse(template.render(context))