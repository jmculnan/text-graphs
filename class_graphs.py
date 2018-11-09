
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

class CreateGraph(object):
    """
    Instances of class CreateGraph are objects that
    take a corpus as input and create a computational
    graph corresponding to the sentences in the input.
    """
    def __init__(self,data):
        self.data   = data
        self.sents  = sent_tokenize(sents)

    
