from django.db import models
from users.models import User


class Artist(models.Model):
    name = models.CharField(max_length=255)


class Album(models.Model):
    name = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist, related_name='albums')
    cover = models.CharField(max_length=255)

    
class Track(models.Model):
    name = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {', '.join(artist.name for artist in self.album.artists)} - {self.name}'


class FavTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'track')

    def __str__(self):
        return str(self.track)