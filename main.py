import tweepy
from listener import Listener

def main():
    # Consumer key, consumer secret, access token, access secret
    ckey = "ayS3T32TuLGG9EQPfeU6czoa0"
    csecret = "5sjr1O9IbpER74v9mcKCBE9ytxMdwMwCDwWKkhiOJAbpJFfDV2"
    atoken = "483349765-nd71tACxbSaU6jmDdwTwH94OVggLLgzYCKMAX6NH"
    asecret = "RT6obqFAW6L9ckaPQgjZY25tyUOonp93x8gtC2eX5kczs"

    # Set up OAuth
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # Stuff we want to search for
    keywords = ["bitcoin", "btc", "satoshi", "xbt"]

    # Start listening
    twitterStream = tweepy.Stream(auth, Listener())
    twitterStream.filter(track=keywords)

main()