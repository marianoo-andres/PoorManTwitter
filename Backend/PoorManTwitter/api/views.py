from rest_framework import viewsets
from . import models, serializers


class TweetViewSet(viewsets.ModelViewSet):
    queryset = models.Tweet.objects.all().order_by('-pk')
    serializer_class = serializers.TweetSerializer
