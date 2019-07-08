from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=50, blank=False)
    message = models.CharField(max_length=50, blank=False)
    created = models.DateTimeField(auto_now_add=True)
