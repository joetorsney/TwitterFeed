import re

""" Returns a tweet in the form of a list of words with all non-alphanumeric characters removed"""
def listifyTweet(data, illegalChars):
    # Illegal chars should be a list of chars to be removed.
    for char in illegalChars:
        data = data.replace(char, "")
    return splitTweet(data)

""" Returns a list of words, @'s and hashtags from a tweet. This also takes into account 
consecutive space characters and does not add them to the return list, unlike .split would. """
def splitTweet(data):
    data = re.sub(" +", " ", data) # Remove all multiple spaces and replace with single space.
    wordList = data.split(" ")
    return wordList
