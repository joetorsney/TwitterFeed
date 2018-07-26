ILLEGAL = {
    "monograms": ["xiang", "huo", "tong", "jia", "airdrop", "free", "retweet", "giveaway", "presale", "sale", "tokensale"],
    "bigrams": ["i copy", "traders automatically", "automatically with", "do you", "listing promotion", "elon musk"],
    "trigrams": ["we are launching", "leverage at bitmex"]
}

ALL_ILLEGAL = ILLEGAL["monograms"] + ILLEGAL["bigrams"] + ILLEGAL["trigrams"]

ILLEGALCHARS = ["\n", "\r", "(", ")", "`", "~", "!", "$", "%", "^", "&", "*", "-", "+", "=", 
                "|", "\\", "{", "}" "[", "]", ":", ";", "\"", "\'", "<", ">", ",", ".", "?", "/"]

ROOT = "./data"
TWEETSPATH = ROOT + "/tweets.csv"
ERRPATH = ROOT + "/err.csv"
SPAMPATH = ROOT + "/spam.csv"