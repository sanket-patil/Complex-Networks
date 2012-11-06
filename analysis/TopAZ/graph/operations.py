import edge
import node

class operations:
    '''Basic operations on a graph: creation, modification, deletion of nodes, edges. '''
    
    def __init__(self, directed = False, weighted = False, nodes = None, edges = None):
        self.nodes = nodes
        self.edges = edges
        if not self.nodes:
            self.nodes = []
        if not self.edges:
            self.edges = []
        self.numnodes = len(self.nodes)
        self.numedges = len(self.edges)
        self.directed = directed
        self.weighted = weighted

    def __del__(self):
        pass

    def getNumNodes(self):
        return self.numnodes

    def getNumEdges(self):
        return self.numedges

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges
    
    def addNode(self, nd):
        if not nd:
            return
        if type(nd) == str:
            if self.getNode(nd):
                return
            self.nodes.append(node.node(str(nd)))
        else:
            if self.getNode(nd.name):
                return
            self.nodes.append(nd)
        self.numnodes += 1        
        return 

    def removeNode(self, nd = None):
        if not nd:
            nd = self.nodes[0]
            for ed in nd.getIncidentEdges():
                self.removeEdge(ed)
            nd.reset()
            self.nodes.remove(nd)
        elif type(nd) == str:
            nd = self.getNode(nd)
            if not nd:
                return
            for ed in nd.getIncidentEdges():
                self.removeEdge(ed)
            nd.reset()
            self.nodes.remove(nd)
        else:
            nd = self.getNode(nd.name)
            if not nd:
                return
            for ed in nd.getIncidentEdges():
                self.removeEdge(ed)
            nd.reset()
            self.nodes.remove(nd)
        self.numnodes -= 1        
        return

    def resetNode(self, nd):
        return nd.reset()

    def addEdge(self, ed, w = 1.0, d = False):
        if not ed:
            return
        if self.isEdgePresent(ed):
            return
        if type(ed) == str:
            e = ed.split()
            h = self.getNode(e[0])
            t = self.getNode(e[1])
            if not h:
                self.addNode(e[0])
                h = self.getNode(e[0])
            if not t:
                self.addNode(e[1])
                t = self.getNode(e[1])           
            ed = edge.edge(e[0], e[1], w, d)
            h.addEdge(ed)
            t.addEdge(ed)
        else:
            h = self.getNode(ed.head)
            t = self.getNode(ed.tail)
            if not h:
                self.addNode(ed.head)
                h = self.getNode(ed.head)
            if not t:
                self.addNode(ed.tail)
                t = self.getNode(ed.tail)
            h.addEdge(ed)
            t.addEdge(ed)
        self.edges.append(ed)
        self.numedges += 1        
        return
    
##    def addEdge(self, head, tail, directed = False, weighted = 1):
##        if not isEdgePresent(head + " " + tail):
##            if not self.getNode(head):
##                self.addNode(node.node(head))
##            if not self.getNode(tail):
##                self.addNode(node.node(tail))
            
    
    def removeEdge(self, ed):
        if not ed:
            return
        if type(ed) == str:
            e = ed.split()
            h = self.getNode(e[0])
            t = self.getNode(e[1])
            if not h or not t:
                return
            ed = self.getEdgeBetween(e[0], e[1])
            if not ed:
                return
            h.removeEdge(ed)
            t.removeEdge(ed)
        else:
            h = self.getNode(ed.head)
            t = self.getNode(ed.tail)
            if not h or not t:
                return
            ed = self.getEdgeBetween(ed.head, ed.tail)
            if not ed:
                return
            h.removeEdge(ed)
            t.removeEdge(ed)
        self.edges.remove(ed)
        self.numedges -= 1
        
        return

    def getEdgeBetween(self, n1, n2):
        ed = n1 + " " + n2
        if self.directed:
            for i in self.edges:
                if i.head + " " + i.tail == ed:
                    return i
        else:
            de = n2 + " " + n1
            for i in self.edges:
                if i.head + " " + i.tail == ed or i.head + " " + i.tail == de:
                    return i
                
        return None        
        
    def resetEdge(self, ed1, ed2):
        pass

    def reverseEdge(self, ed):
        h = ed.tail
        t = ed.head
        d = ed.directed
        w = ed.weight
        self.removeEdge(ed)
        self.addEdge(edge.edge(h, t, w, d))
        return
    
    def isNodePresent(self, nd):
        if not nd:
            return False
        if type(nd) == str:            
            for n in self.nodes:
                if n.name == nd:
                    return True
        else:
            for n in self.nodes:
                if n.name == nd.name:
                    return True
        return False

    def getNode(self, nd):
        for n in self.nodes:
            if n.name == nd:
                return n
        return None

    def isEdgePresent(self, ed):
        if not ed:
            return False
        if type(ed) == str:
            for e in self.edges:
                if e.name == ed:
                    return True
                else:
                    if not self.directed:
                        de = e.tail + ' ' + e.head
                        if de == ed:
                            return True
        else:
            for e in self.edges:
                if e.name == ed.name:
                    return True
                else:
                    if not self.directed:
                        de = e.tail + ' ' + e.head
                        if de == ed.name:
                            return True
        return False

    def getEdge(self, ed):
        for e in self.edges:
            if e.name == ed:
                return e
            else:
                if not self.directed:
                    de = e.tail + ' ' + e.head
                    if de == ed:
                        return e
        return None

    def isGraphEmpty(self):
        if not self.numnodes:
            return True
        return False
    
    def getNeighbours(self, nd):
        neighbours = self.getNode(nd).neighbours
        return [self.getNode(nd) for nd in neighbours]    
    
    def resetNodeColours(self):
        for n in self.nodes:
            n.resetColour()
        return

    def resetNodeVisitedFlags(self):
        for n in self.nodes:
            n.visited = False
        return
    
    def createGraph(self, edgelist, numnodes = -1):
        if not numnodes == -1:
            for i in range(1, numnodes + 1):
                self.addNode(str(i))
        for i in edgelist:
            if not i:
                break
            ed = i.split()
            #if self.isEdgePresent(ed[0] + " " + ed[1]):
            #    continue            
            #if not self.getNode(ed[0]):
            #    self.addNode(node.node(ed[0]))
            #if not self.getNode(ed[1]):
            #    self.addNode(node.node(ed[1]))
            if self.weighted:
                e = edge.edge(ed[0], ed[1], float(ed[2]), self.directed)
            else:
                e = edge.edge(ed[0], ed[1], directed = self.directed)
            self.addEdge(e)
            
        return

    def getEdgeList(self):
        el = []
        for ed in self.edges:
            el.append(ed.head + ' ' + ed.tail)
        return el

    def getNodeList(self):
        nl = []
        for nd in self.nodes:
            nl.append(nd.name)
        return nl
    
    def resetGraph(self):
        while self.nodes:
            self.removeNode()
        return

    def reverseGraph(self):
        for ed in self.edges:
            h = self.getNode(ed.head)
            h.reverseEdge(ed)
            t = self.getNode(ed.tail)
            t.reverseEdge(ed)
            ed.reverse()
        return
        
if __name__ == "__main__":
    print operations.__doc__
    ops = operations()    
##    ops.addNode('1')
##    ops.addNode('2')
##    ops.addNode('3')
##    ops.addNode('1')
##    ops.addNode('2')
##    nd = node.node('5')
##    ops.addNode(nd)    
##    print 'numnodes', ops.numnodes
##    if ops.getNode('5'):
##        print 'Node exists'
##    for i in ops.nodes:
##        print i.name, i.degree
##    print ops.isNodePresent('1')
##    print ops.isNodePresent(node.node('7'))
##    print ops.isNodePresent(node.node('3'))
    print '****'
    #ops.removeNode(node.node('5'))
    ops.createGraph(['7 8', '9 10'])
    #e1 = edge.edge('1', '2')
    #ops.addEdge(e1)
    ops.addEdge('4 6')
    #ops.addEdge(edge.edge('4', '6'))
    print "numedges", ops.numedges
    print "numnodes", ops.numnodes
    for i in ops.nodes:
        print i.name, i.degree
    for e in ops.edges:
        print e.head, e.tail
    print '****'
    print "ed: ", ops.isEdgePresent(edge.edge('1', '2'))    
    ops.removeEdge(edge.edge('1', '2'))
    print "numedges", ops.numedges
    ops.removeNode(node.node('5'))
    for i in ops.edges:
        print i.head, i.tail, i.directed, i.weight
    for i in ops.nodes:
        print i.name, i.degree
    ops.resetGraph()
    for nd in ops.getNodes():
        print 'nd', nd.name
