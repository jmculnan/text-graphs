#helper functions
from nltk.stem import WordNetLemmatizer as wnl
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def addinput(data):
    """
    Read in the data and add to an array
    that is split by sentences.
    """
    with open(data, 'r') as dfile:
        all_data = []
        for line in dfile:
            all_data.append(line.strip())
    return all_data

"""
def preprocess(data):

    Takes a list of sentences and tokenizes,
    lemmatizes, and adds POS-tags.

    processed = []
    for sent in data:
        lems = [wnl().lemmatize(wd) for wd in word_tokenize(sent)]
        sent = pos_tag(word_tokenize(sent))
        pos  = [item[1] for item in sent]
        pairs= list(zip(lems,pos))
        processed.append(pairs)
    return processed
"""
