import json
import csv
import tweepy
import writers
from spamFilter import validTweet
from unidecode import unidecode


class Listener(tweepy.streaming.StreamListener):

    def on_status(self, status):

        try:
            # Filter non-english tweets
            if status.lang != "en":
                return True

            # If tweet is more than 140 chars, it will be 'truncated' and the extended tweet must be accessed.
            if status.truncated:
                text = status.extended_tweet["full_text"]
            else:
                text = status.text
            unix = status.timestamp_ms

            if validTweet(text):
                writers.writeTweet(unix, text)
            else:
                writers.writeSpam(unix, text)
            print(unix)
            print(text + "\n\n###########\n")
        except KeyError as err:
            print(str(err))
        
        print(text)
    def on_error(self, status_code):
        if status_code == 420:
            # If 420, we have been rate limited. Return false and let tweepy handle it.
            return False
        print(status_code)
