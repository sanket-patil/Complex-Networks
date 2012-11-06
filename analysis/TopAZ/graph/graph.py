import operations

class graph:
    '''Stores a graph, its operations and properties.'''
    def __init__(self, directed = False, weighted = False, adjacencylist = None):
        self.directed = directed
        self.weighted = weighted
        self.adjacencylist = adjacencylist
        if not adjacencylist:
            self.adjacencylist = {}
        self.ops = operations.operations(self.directed, self.weighted)
        
    def __del__(self):
        pass

    def addNode(self, node):
        return self.ops.addNode(node)

    def removeNode(self, node):
        return self.ops.removeNode(node)

    def getNode(self, node):
        return self.ops.getNode(node)

    def getNodes(self):
        return self.ops.nodes

    def getNodeList(self):
        return self.ops.getNodeList()
    
    def addEdge(self, edge, weighted = 1, directed = False):
        if self.directed:
            directed = True
        return self.ops.addEdge(edge, weighted, directed)

    def removeEdge(self, edge):
        return self.ops.removeEdge(edge)

    def getEdge(self, edge):
        return self.ops.getEdge(edge)

    def getEdges(self):
        return self.ops.edges
    
    def getEdgeList(self):
        return self.ops.getEdgeList()
    
    def getAdjacencyList(self):
            return self.ops.getAdjacencyList()

    def getReverseAdjacencyList(self):
            return self.ops.getReverseAdjacencyList()

    def create(self, edgelist, numnodes = -1):
        return self.ops.createGraph(edgelist, int(numnodes))
    
    def reverse(self):
        return self.ops.reverseGraph()

    def getReverseGraph(self):
        return self.ops.getReverseGraph()        

    def reset(self):
        return self.ops.resetGraph()

    def resetNodeColours(self):
        return self.ops.resetNodeColours()

    def resetNodeVisitedFlags(self):
        return self.ops.resetNodeVisitedFlags()
    
    def display(self):
        print 'numnodes: ', self.ops.numnodes
        print 'numedges: ', self.ops.numedges
        print 'node, degree'
        for i in self.ops.nodes:
            print i.name, i.degree
        print 'edges'
        for i in self.ops.edges:
            print i.head, i.tail

        return

    def getNumNodes(self):
        return self.ops.numnodes

    def getNumEdges(self):
        return self.ops.numedges
    
    def isGraphConnected(self):
        return self.algorithms.connectivity.connectivity.isGraphConnected()

    def getBFSTree(self):
        return self.analyses.reachability.getBFSTree()

    def getDFSTree(self):
        return self.analyses.reachability.getDFSTree()
        
if __name__ == "__main__":
    print graph.__doc__
    #print dir(graph)
    g = graph(False, False)
    #print g.ops.directed
##    g.create(['1 2', '2 3', '3 4', '7 8', '5 2', '9 8', '10 8'])
##    g.addEdge('5 6')
##    g.addEdge('6 5')
##    g.addEdge('8 7')
##    g.display()
##    print '***'
##    g.removeEdge('2 1')
##    g.display()
##    print g.getEdgeList()
##    print '***'
    g.create(['1 2', '2 3', '3 4', '4 1'], 10)
    g.display()
##    g.reverse()
##    for nd in g.getNodes():
##        print 'nd', nd.name
##        print 'neighbours: ', nd.getNeighbours()
##    g.display()   
##    g.reset()
##    g.display()
    print g.getNodes()
    
