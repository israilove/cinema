from rest_framework import generics
from .models import Actor, Movie
from .serializers import ActorSerializer, MovieSerializer

from cinema.models import Actor, Movie
from datetime import date


class ActorCreateView(generics.CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



actor1 = Actor.objects.create(name='Актер 1', age=30)
actor2 = Actor.objects.create(name='Актер 2', age=35)
actor3 = Actor.objects.create(name='Актер 3', age=40)


movie1 = Movie.objects.create(title='Фильм 1', description='Описание фильма 1', release=date(2023, 1, 1))
movie1.actors.add(actor1, actor2)

movie2 = Movie.objects.create(title='Фильм 2', release=date(2023, 2, 1))
movie2.actors.add(actor1, actor3)
