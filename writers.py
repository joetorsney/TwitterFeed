import csv
from time import time
from constants import *

def writeTweet(unix, text):

    textData = str("\"" + text + "\"")
    rowData = [unix, text]

    with open(TWEETSPATH, "a") as f:
        writer = csv.writer(f)
        writer.writerow(rowData)

def writeErr(text):
    with open(ERRPATH, "a") as f:
        writer = csv.writer(f)
        writer.writerow([time(), text])

def writeSpam(unix, text):
    with open(SPAMPATH, "a") as f:
        writer = csv.writer(f)
        writer.writerow([unix, text])
