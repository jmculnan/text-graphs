
import numpy as np
from helpers import *
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class CreateGraph(object):
    """
    Instances of class CreateGraph are objects that
    take a corpus as input and create a computational
    graph corresponding to the sentences in the input.
    The type of search used must be specified at the
    time of input as 'words' 'lemmas', 'tagged words',
    or 'tagged lemmas'. Default setting is 'words'.
    """
    def __init__(self,data):
        self.data        = data
        self.wds         = [word_tokenize(sent.lower()) for sent in data]
        self.lems        = [wnl().lemmatize(wd) for sent in self.wds for wd in sent]
        self.pos         = [item[1] for sent in self.wds for item in pos_tag(sent)]
        self.connections = np.zeros((len(self.data),len(self.data)))

    def connect_type(self,opt):
        ctype = 'wd'
        if opt == 'words':
            ctype = 'wd'
        elif opt == 'lemmas':
            ctype = 'lem'
        elif opt == 'word_pos':
            ctype = 'wp'
        elif opt == 'lemma_pos':
            ctype = 'lp'

    def getNodeSentence(NodeIdx):
        return

coling = addinput('coling2016_explanation_sentences.txt')
