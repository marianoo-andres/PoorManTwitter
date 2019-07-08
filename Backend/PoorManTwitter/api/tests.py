import itertools
import random
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tweet
from .serializers import TweetSerializer


class TweetTests(APITestCase):
    URL = reverse('tweet-list')
    NUMBER_OF_TWEETS_TO_CREATE = 100

    @staticmethod
    def get_random_tweet_name_message():
        return {'name': 'Tweet' + str(random.randint(0, 10 ** 10)),
                'message': 'Tweet message' + str(random.randint(0, 10 ** 10))}

    def test_list_tweets(self):
        """
            Create tweets via Tweet Model and test that list endpoint
            returns them in the correct order (ordered by descending id).
            Also test returned status codes are valid.
        """
        tweets_data = []
        for _ in range(TweetTests.NUMBER_OF_TWEETS_TO_CREATE):
            tweet = TweetTests.get_random_tweet_name_message()
            tweets_data.insert(0, TweetSerializer(Tweet.objects.create(**tweet)).data)

        response = self.client.get(TweetTests.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for x in range(len(tweets_data)):
            self.assertEqual(response.data[x], tweets_data[x])

    def test_create_tweet(self):
        """
            Create tweets with create endpoint and test the response is valid.
            Also test returned status codes are valid.
        """
        for _ in range(1, TweetTests.NUMBER_OF_TWEETS_TO_CREATE + 1):
            payload = TweetTests.get_random_tweet_name_message()
            response = self.client.post(TweetTests.URL, payload, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data['name'], payload['name'])
            self.assertEqual(response.data['message'], payload['message'])

    def test_create_tweet_without_required_fields(self):
        """
            Try to create tweets with all the combinations of name, message blank or not set.
            Should not be allowed.
        """
        fields = ['name', 'message']
        fields_combinations = []
        for x in range(0, len(fields) + 1):
            for combination in itertools.combinations(fields, x):
                fields_combinations.append(combination)

        for combination in fields_combinations:
            payload = {}  # payload example1: { name: ''} example2: { name: '', message: ''}
            for field in combination:
                payload[field] = ''
            response = self.client.post(TweetTests.URL, payload, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_tweets_and_list(self):
        """
            Create tweets with create endpoint then test that list endpoint returns the
            same tweets created in the correct order (ordered by descending id).
            Also test returned status codes are valid.
        """
        tweets_data = []
        for _ in range(1, TweetTests.NUMBER_OF_TWEETS_TO_CREATE + 1):
            payload = TweetTests.get_random_tweet_name_message()
            response = self.client.post(TweetTests.URL, payload, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            tweets_data.insert(0, response.data)

        response = self.client.get(TweetTests.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for x in range(len(tweets_data)):
            self.assertEqual(response.data[x], tweets_data[x])
