# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Your implementation should pass the tests in test_graph.py.
# KRISTEN ORUE

import functools

class Graph:

    def __init__(self, neighbor = []):
        self.data = {}
        self.neighbor = neighbor

    def adjacent(self, Vertex1, Vertex2):
        if self.data == {}:
          return False
    def neighbors(self, Vertex1):
        if self.adjacent:
            return []
        else:
            return Vertex1

    def add_vertex(self, newVert):
        if self.data.__contains__(newVert):
            pass
        else: 
            self.data[newVert] = self.neighbor
        # self.numVerticies = self.numVerticies + 1
        # newVertex = self.numVerticies
        # return newVertex


    

