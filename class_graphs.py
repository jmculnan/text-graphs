
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
    """
    def __init__(self,data):
        self.wds     = [word_tokenize(sent.lower()) for sent in data]
        self.lems    = [wnl().lemmatize(wd) for sent in self.wds for wd in sent]
        self.pos     = [item[1] for sent in self.wds for item in pos_tag(sent)]
#        self.wd_pos  = ['%s_%s' % (wd, p) for wd in self.wds for p in self.pos]
#        self.lem_pos = ['%s_%s' % (lem, p) for lem in self.lems for p in self.pos]

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


coling = addinput('coling2016_explanation_sentences.txt')
