import json
import csv
import tweepy
from tweetWriter import writeTweet
from unidecode import unidecode


class Listener(tweepy.streaming.StreamListener):

    def on_data(self, data):

        try:
            data = json.loads(data) # Convert into python object
            text = unidecode(data["text"]) # Decode unicode
            unix = data["timestamp_ms"]

            writeTweet(unix, text)
            
            print(unix)
            print(text + "\n\n###########\n")
        except KeyError as err:
            print(str(err))

        return True

    def on_error(self, status_code):
        if status_code == 420:
            # If 420, we have been rate limited. Return false and let tweepy handle it.
            return False
        print(status_code)