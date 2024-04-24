from django.db import models

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=100)

class Title(models.Model):
    TYPE_CHOICES = [('Movie', 'Movie'), ('TV Show', 'TV Show')]
    show_id = models.CharField(max_length=100)  # Not unique accross datasets
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name='titles')
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255, blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=50, blank=True, null=True)
    duration = models.CharField(max_length=100)

    class Meta:
        unique_together = ('show_id', 'platform')  # Ensures combination of show_id and platform is unique