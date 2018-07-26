from listifyTweet import listifyTweet
from findNgrams import ngramsRangeFromList
from constants import *

def validTweet(text):
    monograms = listifyTweet(text, ILLEGALCHARS)
    ngrams = ngramsRangeFromList(monograms, 3)

    for ngram in ngrams:
        if ngram.lower() in ALL_ILLEGAL:
            return False

    return True
