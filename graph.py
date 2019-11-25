# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Your implementation should pass the tests in test_graph.py.
# KRISTEN ORUE

import functools

class Graph:

    def __init__(self):
        self.data = {}

    def adjacent(self, Vertex1, Vertex2):
        if self.data == {}:
          return False

        elif Vertex2 in self.data[Vertex1]:
            return True 
        else:
            return False

    def neighbors(self, vertex1):
        if vertex1 not in self.data:
            return []
        else:
            return self.data[vertex1]


    def add_vertex(self, newVert):
        if self.data.__contains__(newVert):
            pass
        else: 
            self.data[newVert] = []
        # self.numVerticies = self.numVerticies + 1
        # newVertex = self.numVerticies
        # return newVertex
    def remove_vertex(self, vertice): 
        if vertice in self.data:
            for vertex in self.data[vertice]:
                self.data[vertex].remove(vertice)
            del self.data[vertice]
        else:
            pass
 
        # if vertice in self.data[vertice]:
        #     del vertice
        # if self.data.__contains__(vertice):
        #     del self.data[vertice]

    def add_edge(self, vertex1, vertex2):
        # if self.data.__contains__(vertex1):
        #     self.data[vertex1].append(vertex2)
        if self.data.__contains__(vertex1) and self.data.__contains__(vertex2):
            if self.data[vertex1].__contains__(vertex2) and self.data[vertex2].__contains__(vertex1):
                pass
            else:
                self.data[vertex1].append(vertex2)   
                self.data[vertex2].append(vertex1) 
        else: 
            pass

    def remove_edge(self, vertex1, vertex2):
        if self.data.__contains__(vertex1) and self.data.__contains__(vertex2):
            if vertex2 in self.data[vertex1]:
                self.data[vertex1].remove(vertex2)
                self.data[vertex2].remove(vertex1)
        else:
            pass
    def v(self):
        return len(self.data)

    def e(self):
        n=0
        for vertex in self.data.keys():
            n += len(self.data[vertex])
        return n/2

        # for vertice in self.data:
        #  return len(self.data[vertice])
 





    

