import csv

def writeTweet(unix, text):

    textData = str("\"" + text + "\"")
    rowData = [unix, text]

    with open("tweets.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(rowData)
