import edge

class node:
    '''Stores info about nodes in a graph.
    Degrees, Neighbours etc..'''
    def __init__(self, name):
        self.name = name
        self.colour = "white"
        self.visited = False
        self.degree = 0
        self.indegree = 0
        self.outdegree = 0
        self.edgelist = []
        self.neighbours = []
        self.neighbourhood = []
        self.inedgelist = []
        self.outedgelist = []

    def setName(newname):
        self.name = newname
        return

    def getName(self):
        return self.name
    
    def setColour(clr):
        self.colour = clr
        return

    def getColour(self):
        return self.colour
    
    def resetColour():
        self.colour = "white"
        return

    def setVisited(self):
        self.visited = True
        return

    def getVisited():
        return self.visited
    
    def resetVisited():
        self.visited = False
        return
    
    def addEdge(self, ed):
        if ed.directed:
            if ed.head == self.name:
                self.outedgelist.append(ed)
                self.outdegree += 1
                self.degree += 1
                self.neighbours.append(ed.tail)
                self.neighbourhood.append(ed.tail)
            elif ed.tail == self.name:
                self.inedgelist.append(ed)
                self.indegree += 1
                self.neighbourhood.append(ed.head)
        else:
            if ed.head == self.name:
                self.neighbours.append(ed.tail)
                self.neighbourhood.append(ed.tail)
                self.edgelist.append(ed)
                self.degree += 1
            elif ed.tail == self.name:
                self.neighbours.append(ed.head)
                self.neighbourhood.append(ed.head)
                self.edgelist.append(ed)
                self.degree += 1
            else:
                return           
        return

    def removeEdge(self, ed):
        if ed.directed:
            if ed.head == self.name:
                for e in self.outedgelist:
                    if e.tail == ed.tail:
                        self.outedgelist.remove(e)
                        self.outdegree -= 1
                        self.degree -= 1
                        self.neighbours.remove(e.tail)
                        self.neighbourhood.remove(e.tail)
                        break
            elif ed.tail == self.name:
                for e in self.inedgelist:
                    if e.head == ed.head:                    
                        self.inedgelist.remove(e)
                        self.indegree -= 1
                        self.neighbourhood.remove(e.head)
                        break
        else:
            for e in self.edgelist:
                if (ed.head == e.head and ed.tail == e.tail) or (ed.head == e.tail and ed.tail == e.head):
                    self.edgelist.remove(e)
                    self.degree -= 1
                    break
            if ed.head == self.name:                
                self.neighbours.remove(ed.tail)
                self.neighbourhood.remove(ed.tail)
            else:
                self.neighbours.remove(ed.head)
                self.neighbourhood.remove(ed.head)
        return

    def reverseEdge(self, ed):
        if ed.directed:
            if ed.head == self.name:
                for e in self.outedgelist:
                    if e.tail == ed.tail:
                        self.outedgelist.remove(e)
                        self.inedgelist.append(e)
                        self.outdegree -= 1
                        self.degree -= 1
                        self.indegree += 1
                        self.neighbours.remove(e.tail)
                        break
            elif ed.tail == self.name:
                for e in self.inedgelist:
                    if e.head == ed.head:
                        self.inedgelist.remove(e)
                        self.outedgelist.append(e)
                        self.indegree -= 1
                        self.outdegree += 1
                        self.degree += 1
                        self.neighbours.append(e.head)
                        break
        return
    
    def getNeighbours(self):
        return self.neighbours

    def getNeighbourhood(self):
        return self.neighbourhood

    def isInNeighbourhood(self, nd):
        return nd in self.neighbourhood
    
    def getIncidentEdges(self):
        return self.edgelist + self.inedgelist + self.outedgelist

    def getOutEdges(self):
        return self.outedgelist

    def getInEdges(self):
        return self.inedgelist

    def getOutEdgeList(self):
        outel = []
        for ed in self.outedgelist:
            outel.append(ed.head + ' ' + ed.tail)
        return outel

    def getInEdgeList(self):
        inel = []
        for ed in self.inedgelist:
            inel.append(ed.head + ' ' + ed.tail)
        return inel

    def getEdgeList(self):
        el = []
        for ed in self.edgelist:
            el.append(ed.head + ' ' + ed.tail)
        for ed in self.outedgelist:
            el.append(ed.head + ' '+ ed.tail)
        return el

    def getIncidentEdgeList(self):
        iel = []
        for ed in self.edgelist:
            iel.append(ed.head + ' ' + ed.tail)
        for ed in self.outedgelist:
            iel.append(ed.head + ' ' + ed.tail)
        for ed in self.inedgelist:
            iel.append(ed.head + ' ' + ed.tail)
        return iel

    def reset(self):
        del self.edgelist[:]
        del self.neighbours[:]
        del self.inedgelist[:]
        del self.outedgelist[:]
        self.degree = self.indegree = self.outdegree = 0
        self.colour = "white"
        self.visited = "False"
        return

    
if __name__ == "__main__":
    print node.__doc__
    n1 = node('1')
    n2 = node('2')
    print "node names", n1.name, n2.name
    e = edge.edge('1', '2')    
    n1.addEdge(e)
    e = edge.edge('2', '1')
    n2.addEdge(e)
    n1.addEdge(edge.edge('5', '1'))
    print "degrees", n1.degree, n2.degree
    e = edge.edge('4', '1', directed = True)
    n1.addEdge(e)
    e = edge.edge('1', '7', directed = True)
    n1.addEdge(e)
    print 'neighbourhood:', n1.getNeighbourhood()
    for e in n1.getEdgeList():
        print e
    n1.removeEdge(edge.edge('1', '7', directed = True))
    print 'neighbourhood:', n1.getNeighbourhood()
    for e in n1.getEdgeList():
        print e
    print('\n')
    n1.removeEdge(edge.edge('2', '1'))
    print 'neighbourhood:', n1.getNeighbourhood()
    for e in n1.getEdgeList():
        print e
    n1.reset()
    print "n1: " 
    for e in n1.getEdgeList():
        print e    
