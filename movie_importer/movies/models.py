from django.db import models


class Name(models.Model):
    imdb_name_id = models.CharField(max_length=20, unique=True)
    primary_name = models.CharField(max_length=120)
    birth_year = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    primary_profession = models.CharField(max_length=250)

    def __str__(self):
        return self.primary_name

    class Meta:
        ordering = ('imdb_name_id',)


class Title(models.Model):
    imdb_title_id = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=120)
    primary_title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    is_adult = models.BooleanField()
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    runtime_minutes = models.IntegerField(blank=True, null=True)
    genres = models.CharField(max_length=250)
    author = models.ForeignKey(Name, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.original_title

    class Meta:
        ordering = ('imdb_title_id',)
