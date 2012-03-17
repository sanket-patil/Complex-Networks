''' Stores a path in a graph. '''

class path:
    def __init__(self, p = None, weight = 0.0):
        self.nodesinpath = p
        if not self.nodesinpath:
            self.nodesinpath = []
        self.length = 0
        if len(self.nodesinpath) > 0:
            self.length = len(self.nodesinpath) - 1
        if not weight:
            self.weight = self.length
        else:
            self.weight = weight
#        if w:
 #           self.weightv.append(w)
  #          self.weight = sum(self.weightv)
        
        
    def getSource(self):
        return self.nodesinpath[0]

    def getDestination(self):
        return self.nodesinpath[-1]

    def getIntermediateNodes(self):
        return self.nodesinpath[1:-1]

    def getPathLength(self):
        #return len(self.nodesinpath) - 1
        return self.weight
    
    def getPathWeight(self):
        return self.weight
    
    def isNodeInPath(self, nd):
        return nd in self.nodesinpath

    def isIntermediateNode(self, nd):
        return nd in self.getIntermediateNodes()

    def isPathBetween(self, src, dest):
        return src == self.getSource() and dest == self.getDestination()

    def isEdgeInPath(self, ed):
        ed = ed.split()
        h = ed[0]
        t = ed[1]
        if h == self.getDestination():
            return False
        if h in self.nodesinpath:
            i = self.nodesinpath.index(h)
            if t == self.nodesinpath[i + 1]:
                return True
        return False
    
    def addNode(self, nd, w = 1.0):
        self.nodesinpath.append(nd)
        self.length += 1
        if self.weightv:
            self.weightv.append(w)
        self.weight += w
        return

    def removeNode(self, nd = None):
        if nd:
            if nd in self.nodesinpath:
                index = self.nodesinpath.index(nd)
                self.nodesinpath.remove(nd)
                self.length -= 1
                if self.weightv:
                    w = self.weightv.pop(index)
                    self.weight -= w
        else:
            self.nodesinpath.pop(0)
            if self.weightv:
                w = self.weightv.pop(0)
                self.weight -= w
            self.length -= 1
        return

    def resetPath(self):
        while len(self.nodesinpath):
            self.removeNode()
        self.length = 0
        if self.weightv:
            del self.weightv[:]
        self.weight = 0
        return
    
    def getPathString(self):
        pathstr = ''
        for nd in self.nodesinpath:
            pathstr += nd + ' '
        return pathstr
    
    def reverse(self):
        if self.nodesinpath:
            self.nodesinpath.reverse()
        if self.weightv:
            self.weightv.reverse()
        return

    def getReversePath(self):
        return self.nodesinpath[::-1]

    def getReversePathString(self):
        revpathstr = ''
        for nd in self.nodesinpath[::-1]:
            revpathstr += nd + ' '
        return revpathstr

    def getEdgesInPath(self):
        el = []
        for i in range(self.length):
            e = self.nodesinpath[i] + ' ' + self.nodesinpath[i + 1]
            el.append(e)
        return el
    
    def sharesEdgesWithPath(self, el1):
        el = self.getEdgesInPath()
        for e in el1:
            if e in el:
                return True
        return False

if __name__ == "__main__":
    p = path(['1', '2', '4', '7', '32'])
    print p.getSource()
    print p.getDestination()
    print p.getPathLength()
    print p.isNodeInPath('5')
    print p.isNodeInPath('4')
    print p.getIntermediateNodes()
    p = path(['7', '6', '10' , '32' , '87', '36'])
    print p.isIntermediateNode('7')
    print p.isIntermediateNode('9')
    print p.getPathString()
    p.reverse()
    print p.nodesinpath
    p.reverse()
    print p.nodesinpath
    print p.getReversePath()
    print p.getReversePathString()
    print p.nodesinpath
    p.addNode('15')
    print p.getPathLength()
    print p.nodesinpath
    p.removeNode('2')
    print p.nodesinpath
    print p.isPathBetween('1', '32')
    print p.isPathBetween('1', '15')
    print 'ed:', p.isEdgeInPath('6 10')
    print p.nodesinpath
    print 'pathlength', p.getPathLength()
    print 'edges:', p.getEdgesInPath()
    print 'shares:', p.sharesEdgesWith(['1 2', '7 10', '36 16'])
    p.resetPath()
    print 'nodes', p.nodesinpath
    print p.getPathLength()
