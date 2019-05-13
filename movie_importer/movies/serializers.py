from rest_framework import serializers

from .models import Title, Name


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    author = NameSerializer(read_only=True)

    class Meta:
        model = Title
        fields = ('imdb_title_id', 'type', 'primary_title', 'original_title', 'is_adult', 'start_year', 'end_year',
                  'runtime_minutes', 'genres', 'author')
