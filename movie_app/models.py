from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.director_movies.count()


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director_movies')
    genres = models.ManyToManyField(Genre, related_name='genre_movies')

    def __str__(self):
        return self.title

    def director_name(self):
        if self.director:
            return self.director.name
        return None

    @property
    def rating(self):
        reviews = self.movie_reviews.all()
        return sum(review.stars for review in reviews) / len(reviews) if reviews else 0


class Review(models.Model):
    STAR_CHOICES = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reviews')
    stars = models.PositiveSmallIntegerField(choices=STAR_CHOICES)

    def __str__(self):
        return self.text[:50]
