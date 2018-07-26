"""Given a list of words this returns a list of all ngrams within that list"""
def ngramsFromList(data, n):
    ngram = []
    ngrams = []

    for i in range(0, len(data)-n+1):
        ngram = (data[i:i+n])
        ngram = " ".join(ngram)
        ngrams.append(ngram)

    return ngrams

""" Given a list of words this returns a list of all (1, 2, ..., n)grams in that list"""
def ngramsRangeFromList(data, n):
    ngramsRange = []
    ngramsRange += data

    for i in range(2, n+1):
        ngramsRange += ngramsFromList(data, i)
    
    return ngramsRange
