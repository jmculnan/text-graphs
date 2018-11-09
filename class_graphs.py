
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
        self.data  = data
        self.wds   = [word_tokenize(sent.lower()) for sent in data]
        self.lems  = [wnl().lemmatize(wd) for sent in self.wds for wd in sent]
        self.pos   = [item[1] for sent in self.wds for item in pos_tag(sent)]
        self.ctype = 'wd' #used for connection type; may be changed with connect_type

    def connect_type(self,opt):
        """
        Use this method to change connection type to
        be used when comparing sentences in the graph.
        """
        if opt == 'lemmas':
            self.ctype = 'lem'
        elif opt == 'word_pos':
            self.ctype = 'wp'
        elif opt == 'lemma_pos':
            self.ctype = 'lp'
        else:
            self.ctype = 'wd'

    def exportToDOT(self)

    def getNodeSentence(self, NodeIdx):
        """
        Given a node index, return the corresponding
        sentence.
        """
        return self.data[NodeIdx]

    def getEdgeWeightBetweenNodes(self,NodeIdx1,NodeIdx2):
        """
        Calculate the number of items in common between two nodes
        """
        if self.ctype == 'lem':
            sent1 = self.lems[NodeIdx1]
            sent2 = self.lems[NodeIdx2]
        elif self.ctype == 'wp':
            sent1 = list(zip(self.wds[NodeIdx1],self.pos[NodeIdx1]))
            sent2 = list(zip(self.wds[NodeIdx2],self.pos[NodeIdx2]))
        elif self.ctype == 'lp':
            sent1 = list(zip(self.lems[NodeIdx1],self.pos[NodeIdx1]))
            sent2 = list(zip(self.lems[NodeIdx2],self.pos[NodeIdx2]))
        else:
            sent1 = self.wds[NodeIdx1]
            sent2 = self.wds[NodeIdx2]
        return count_common_points(sent1,sent2)

    def size(self):
        return len(self.data) ** 2 - len(self.data)

coling = addinput('coling2016_explanation_sentences.txt')
