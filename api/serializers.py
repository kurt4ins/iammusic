from rest_framework import serializers
from api.models import Artist, Album, Track, FavTrack


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]


class AlbumSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Album
        fields = ["id", "name", "artists", "cover"]


class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = Track
        fields = ["id", "name", "spotify_id", "album"]


class FavTrackSerializer(serializers.ModelSerializer):
    track = TrackSerializer()
    
    class Meta:
        model = FavTrack
        fields = ["user", "track", "date_added"]
