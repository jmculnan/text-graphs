
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
        self.ctype = 'wd' #used for connection type; may be changed with connect_type
        self.graph = np.zeros((len(self.data),len(self.data))) #larger than we need

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
                if i < j: #don't duplicate--this should be a triangle matrix
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


    def exportToDOT(self,fname='my_graph.dot', section_size = 10):
        """
        Export the graph to .dot file. This was way too large,
        so I've allowed for the number of sentences selected
        from the dataset to be altered. Sentences that have
        no connections to any other within the subset are not
        shown in the graph.
        """
        with open(fname,'w') as graphfile:
            graphfile.write('digraph D {\n\nnode [shape=record];\nedge [arrowhead=none];\n\n')
            for i, node in enumerate(self.data):
                if i < section_size:
                    opts = []
                    wgts = []
                    for j in range(section_size):
    #            for j in range(len(self.data)):
                        if self.graph[i][j] != 0 and i != j:
                            graphfile.write('"%s" -> "%s" [penwidth=%d, label = "%d"]\n' % \
                            (node, self.data[j], self.graph[i][j], self.graph[i][j]))
    #                        opts.append(self.data[j])
        #                    wgts.append(self.graph[i][j])
    #                opts = ', '.join(opts.remove('.'))
    #                graphfile.write('%d -> {%s}\n' % (i, opts) )
    #                graphfile.write('%s -> {%s}\n' % (node, opts) )
            graphfile.write('\n}')

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
        return self.graph[NodeIdx1][NodeIdx2]

    def size(self):
        return len(self.data)

    def findShortestPaths(NodeIdx1, NodeIdx2):
        """
        Find the shortest path between any two nodes.
        Do a breadth-first search
        """
        pointers = []
        point = NodeIdx1
#        while pointers[-1] != NodeIdx2:
        for i in range(length(graph)):
            if graph[i] != point and (graph[point][i] != 0 or \
            graph[i][point] != 0):
                    nextlayer += 1
                    pointers.append((NodeIdx1, i))


coling = addinput('coling2016_explanation_sentences.txt')
