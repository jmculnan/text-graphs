# text-graphs
Code for creating, storing, and working with a text graph

This code is written for python 3.X and assumes the ability to run nltk and its dependency packages.

class_graphs.py contains the class CreateGraph built-in functions for this class:
  1. connect_type: to change between connection types when comparing sentences
  2. populate_graph: to calculate similarities between nodes for the current connection type (self.ctype)
  3. exportToDOT: to export the graph as a .dot file
  4. getNodeSentence: return the sentence for a given node
  5. getEdgeWeightBetweenNodes: to return similarity of two nodes
  6. size: to report the number of nodes
  7. findShortestPaths: to find the shortest path between two nodes; currently incomplete

helpers.py contains functions to read input and count the number of items shared between two lists. These functions are used by instances of class CreateGraph.

The Graphs directory contains .dot files containing subgraphs with a portion of the total nodes and .pdf files produced from those .dot files. Files are named after the connection type and number of nodes examined.

Finally, Built-in_Output.html is an html file containing the output of a Jupyter Notebook demonstrating how the built-in functions in 4-6 above work.
