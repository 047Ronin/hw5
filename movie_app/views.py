from movie_app.serializers import DirectorSerializers, MovieSerializersList, ReviewSerializers
from movie_app.models import Director, Movie, Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination


class DirectorCreateListAPIVeiw(ListCreateAPIView):
    queryset = Director.objects.get_queryset().order_by('id')
    serializer_class = DirectorSerializers
    pagination_class = PageNumberPagination


class DirectorDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers


class MovieCreateListAPIVeiw(ListCreateAPIView):
    queryset = Director.objects.get_queryset().order_by('id')
    serializer_class = MovieSerializersList
    pagination_class = PageNumberPagination


class MovieDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializersList


class ReviewCreateListAPIVeiw(ListCreateAPIView):
    queryset = Review.objects.get_queryset().order_by('id')
    serializer_class = ReviewSerializers
    pagination_class = PageNumberPagination


class ReviewDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
