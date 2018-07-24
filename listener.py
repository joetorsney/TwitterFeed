import json
import tweepy
from unidecode import unidecode
from database import Database


class Listener(tweepy.streaming.StreamListener):

    def __init__(self):
        self.db = Database("Tweets")

    def on_data(self, data):
        data = json.loads(data) # Convert into python object
        text = unidecode(data["text"]) # Decode unicode
        unix = data["timestamp_ms"]

        self.db.addTweet(unix, text) # Save to database
        print(unix)
        print(text + "\n\n###########\n")
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # If 420, we have been rate limited. Return false and let tweepy handle it.
            return False
        print(status_code)