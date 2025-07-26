from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'spotify_id', 'email', 'display_name']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists")
        return value

        