from rest_framework import serializers
from movie_app.models import Director, Movie, Review
#from movie_app import views


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name count_movies movies'.split()


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description director reviews rating'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class DirectorCountSerialize(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movie_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()
