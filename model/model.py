import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._idMap={}


    def buildgraph(self,anno):
        self._nodes = DAO.getNodes(anno)
        for i in self._nodes:
            self._idMap[i.CCode]=i
        self._edges = DAO.getEdges(anno)
        self._graph.add_nodes_from(self._nodes)
        #self._graph.add_edges_from(self._edges)
        for i in self._edges:
            self._graph.add_edge(self._idMap[i.stato1],self._idMap[i.stato2])

    def getNodes(self):
        return self._nodes
    def getNumNodes(self):
        return len(self._nodes)

    def getNumEdges(self):
        return len(self._edges)