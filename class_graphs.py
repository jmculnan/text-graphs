
import numpy as np
from helpers import *
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer as wnl

class CreateGraph(object):
    """
    Instances of class CreateGraph are objects that
    take a corpus as input and create a computational
    graph corresponding to the sentences in the input.
    """
    def __init__(self,data):
        self.data  = data
        self.wds   = [word_tokenize(sent.lower()) for sent in data]
        self.lems  = [[wnl().lemmatize(wd) for wd in sent] for sent in self.wds]
        self.pos   = [[pos for (wd,pos) in pos_tag(sent)] for sent in self.wds]
#        self.pos   = [item[1] for sent in self.wds for item in pos_tag(sent)]
        self.ctype = 'wd' #used for connection type; may be changed with connect_type
        self.graph = np.zeros((len(self.data),len(self.data)))

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

    def populate_graph(self):
        """
        Populate the empty graph with weights based on connection type
        """
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.ctype == 'lem':
                    self.graph[i][j] = count_common_points(self.lems[i],self.lems[j])
                elif self.ctype == 'wp':
                    sent1 = list(zip(self.wds[i],self.pos[i]))
                    sent2 = list(zip(self.wds[j],self.pos[j]))
                    self.graph[i][j] = count_common_points(sent1, sent2)
                elif self.ctype == 'lp':
                    sent1 = list(zip(self.lems[i],self.pos[i]))
                    sent2 = list(zip(self.lems[j],self.pos[j]))
                    self.graph[i][j] = count_common_points(sent1, sent2)
                else:
                    self.graph[i][j] = count_common_points(self.wds[i],self.wds[j])


    def exportToDOT(self):
        pass

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
        return self.graph[NodeIdx1,NodeIdx2]

    def size(self):
        return len(self.data) ** 2 - len(self.data)

coling = addinput('coling2016_explanation_sentences.txt')
