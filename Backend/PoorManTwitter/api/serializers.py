from rest_framework import serializers
from . import models


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'message',
            'created'
        )
        model = models.Tweet
