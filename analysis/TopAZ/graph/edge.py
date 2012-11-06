class edge:
    ''' The 'edge' class stores info about an edge in a graph.
    Edges can be directed or undirected and/or weighted.'''
    def __init__(self, head, tail, weight = 1, directed = False):
        self.head = head
        self.tail = tail
        self.name = head + " " + tail
        self.weight = weight
        self.directed = directed    

    def getEdgename(self):
        return self.name

    def resetEdge(self, h, t, w = 1, d = False):
        self.head = h
        self.tail = t
        self.weight = w
        self.directed = d
        return

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        return
    
    def setWeight(self, w):
        self.weight = w
        return

    def makeDirected(self):
        self.directed = True
        return

    def makeUndirected(self):
        self.directed = False
        return
    
if __name__ == '__main__':
    print edge.__doc__
    e = edge('1', '2')
    print e.head, e.tail, e.directed, e.weight
    e.makeDirected()
    e.setWeight(10)
    print e.head, e.tail, e.directed, e.weight
    e.resetEdge('3', '4')
    print e.head, e.tail, e.directed, e.weight
