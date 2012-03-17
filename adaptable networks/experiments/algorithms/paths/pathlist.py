''' A list of paths. '''

import path

class pathlist:
    def __init__(self, paths = None):
        self.paths = paths
        if paths:
            self.paths = paths
            self.numpaths = len(paths)
        else:
            self.paths = []        
            self.numpaths = 0

    def addPath(self, p):
        if not self.paths:
            self.paths = [] 
        self.paths.append(p)
        self.numpaths += 1
        return

    def removePath(self, p = None):
        if p:
            p = p.getPathString()
            for q in self.paths:
                if q.getPathString() == p:
                    self.paths.remove(q)
                    self.numpaths -= 1
        else:
            self.paths.pop(0)
            self.numpaths -= 1
        return

    def replacePath(self, p, q):
        self.removePath(p)
        self.addPath(q)
        return

    def getPath(self, p = None):
        if not p:
            if self.numpaths > 0:
                return self.paths[0]
        return None
    
    def reset(self, p = None):
        while self.numpaths:
            self.removePath()
        if p:
            self.paths = p

        return        

    def isPathInList(self, p):
        p = p
        if not type(p) == str:
            p = p.getPathString()
        for q in self.paths:
            if p == q.getPathString():
                return True
        return False
            
    def getPathList(self):
        return self.paths
    
    def getNumPaths(self):
        return self.numpaths
    
    def getLongestPath(self):
        lp = self.getPath()
        if not lp:
            return None
        lpl = lp.getPathLength()
        for p in self.paths[1:]:
            pl = p.getPathLength()
            if pl > lpl:
                lpl = pl
                lp = p
        return lp
    
    def getShortestPath(self):
        sp = self.getPath()
        spl = sp.getPathLength()
        for p in self.paths[1:]:
            pl = p.getPathLength()
            if pl < spl:
                spl = pl
                sp = p
        return sp

    def getPathsBetween(self, src, dest):
        plist = []
        for p in self.paths:
            if p.isPathBetween(src, dest):
                plist.append(p)
        return plist

    def getNumPathsBetween(self, src, dest):
        paths = self.getPathsBetween(src, dest)
        if paths:
            return len(paths)
        return 0

    def getShortestPathsBetween(self, src, dest):
        plist = self.getPathsBetween(src, dest)
        if not plist:
            return None
        else:
            return self.getShortestPaths(plist)
        
    def getShortestPaths(self, plist = None):
        plist = plist
        spl = 0
        splist = []
        if plist:
            spl = plist[0].getPathLength()
            splist.append(plist[0])
        else:            
            plist = self.paths
            splist = [self.getPath()]        
            spl = splist[0].getPathLength()
        for p in plist[1:]:
            pl = p.getPathLength()
            if pl > spl:
                continue
            elif pl == spl:
                splist.append(p)
            else:
                while splist:
                    splist.pop()
                splist.append(p)
                spl = pl
        return splist
    
    def getNumShortestPathsBetween(self, src, dest):
        paths = self.getShortestPathsBetween(src, dest)
        if paths:
            return len(paths)
        return 0

    def getPathsFrom(self, src):
        plist = []
        for p in self.paths:
            if p.getSource() == src:
                plist.append(p)
        return plist
    
    def getShortestPathsFrom(self, src):
        plist = self.getPathsFrom(src)
        if not plist:
            return None
        else:
            return self.getShortestPaths(plist)
            
    def getPathsTo(self, dest):
        plist = []
        for p in self.paths:
            if p.getDestination() == dest:
                plist.append(p)
        return plist

    def getShortestPathsTo(self, src):
        plist = self.getPathsTo(dest)
        if not plist:
            return None
        else:
            return self.getShortestPaths(plist)
        
    def getPathsThroughNode(self, inter, src = None, dest = None):        
        if src and dest:
            pbetween = self.getPathsBetween(src, dest)
            if not pbetween:
                return None
            pthrough = []
            for p in pbetween:
                if p.isIntermediateNode(inter):
                    pthrough.append(p)
            return pthrough
        if not src and not dest:
            pthrough = []
            for p in self.paths:
                if p.isIntermediateNode(inter):
                    pthrough.append(p)
            return pthrough
        return None

    def getNumPathsThroughNode(self, inter, src = None, dest = None):
        paths = self.getPathsThroughNode(inter, src, dest)
        if paths:
            return len(paths)
        return 0
    
    def getShortestPathsThroughNode(self, inter, src = None, dest = None):
        if src and dest:
            pbetween = self.getShortestPathsBetween(src, dest)
            if not pbetween:
                return None
            pthrough = []
            for p in pbetween:                
                if p.isIntermediateNode(inter):
                    pthrough.append(p)
            return pthrough
        if not src and not dest:
            pthrough = self.getPathsThroughNode(inter)
            return self.getShortestPaths(pthrough)
        return None
    
    def getNumShortestPathsThroughNode(self, inter, src = None, dest = None):
        paths = self.getShortestPathsThroughNode(inter, src, dest)
        if paths:
            return len(paths)
        return 0
    
    def getPathsThroughEdge(self, ed, src = None, dest = None):
        if src and dest:
            pbetween = self.getPathsBetween(src, dest)
            if not pbetween:
                return None
            pthrough = []
            for p in pbetween:
                if p.isEdgeInPath(ed):
                    pthrough.append(p)
            return pthrough
        if not src and not dest:
            pthrough = []
            for p in self.paths:
                if p.isEdgeInPath(ed):
                    pthrough.append(p)
            return pthrough
        return None
    
    def getNumPathsThroughEdge(self, ed, src = None, dest = None):
        paths = self.getPathsThroughEdge(ed, src, dest)
        if paths:
            return len(paths)
        return 0

    def getShortestPathsThroughEdge(self, ed, src = None, dest = None):
        if src and dest:
            pbetween = self.getShortestPathsBetween(src, dest)
            if not pbetween:
                return None
            pthrough = []
            for p in pbetween:                
                if p.isEdgeInPath(ed):
                    pthrough.append(p)
            return pthrough
        if not src and not dest:
            pthrough = self.getPathsThroughEdge(ed)
            return self.getShortestPaths(pthrough)
        return None
    
    def getNumShortestPathsThroughEdge(self, ed, src = None, dest = None):
        paths = self.getPathsThroughEdge(ed, src, dest)
        if paths:
            return len(paths)
        return 0

    def getEdgeIndependentPaths(self, src = None, dest = None):
        ip = []
        if not src and not dest:
            np = self.getNumPaths()
            for i in range(np):
                for j in range(i, np):
                    if i == j:
                        continue
                    p1 = self.paths[i]
                    p2 = self.paths[j]                    
                    #if p1.getPathLength() < p2.getPathLength():
                    if p2.sharesEdgesWithPath(p1.getEdgesInPath()):
                        if p1.getPathLength() > p2.getPathLength():
                            toremove.append(p1)
                        else:
                            toremove.append(p2)
            for p in toremove:
                self.removePath(p)
            del toremove[:]
            return
        else:
        # Need to implement the other case
            pass
        
    def getNumEdgeIndependentPaths(self, src = None, dest = None):
        if self.getNumPaths() < 2:
            return self.getNumPaths()
        self.getEdgeIndependentPaths(src, dest)
        return self.getNumPaths()

    def isPathEdgeIndependent(self, q):
        for p in self.paths:
            if p.sharesEdgesWithPath(q.getEdgesInPath()):
                return False
        return True
        
if __name__ == "__main__":
    print __doc__
    p = path.path(['1', '5', '7', '8', '16'])    
    q = path.path(['2', '5'])
    pl = {}
    for i in range(3):
        pl[i] = pathlist()
    pl[0].addPath(p)

    for k,v in pl.iteritems():
        print k
        for p in v.getPathList():
            print p.getPathString()
    pl[1].addPath(q)
    q = q.nodesinpath
    q.append('3')
    q = path.path(q)
    pl[2].addPath(q)
    for k,v in pl.iteritems():
        print k
        for p in v.getPathList():
            print p.getPathString()
    
        
##    pl = pathlist([p])
##    pl1 = pathlist()
##    p = path.path(['1', '5', '6', '7', '8', '16'])    
##    pl.addPath(p)
##    p = path.path(['7', '6', '9' , '32' , '87', '36'])
##    pl.addPath(p)
##    p = path.path(['7', '6', '10' , '32' , '87', '36'])
##    pl.addPath(p)
##    p = path.path(['7', '5', '10' , '32' , '87', '36'])
##    pl.addPath(p)
##    p = path.path(['7', '6', '9' , '32' , '72', '85', '36'])
##    pl.addPath(p)
##    print 'pl1', pl1.paths
##    print pl.paths
##    print pl.numpaths
##    q = path.path(['1', '5', '7', '9', '16'])    
##    print pl.isPathInList(q)
##    q = path.path(['1', '5', '7', '8', '16', '10', '2'])
##    if not pl.isPathInList(q):
##        pl.addPath(q)
##    print "All Paths"
##    for p in pl.getPathsBetween('7', '36'):
##        print p.getPathString()
##    #print '\n'
##    print pl.getNumPathsBetween('7', '36')
##    print '\n'
##    print "Shortest Paths"
##    for p in pl.getShortestPathsBetween('7', '36'):
##        print p.getPathString()
##    print '\n'    
##    print pl.getNumShortestPathsBetween('7', '36')
##    print '\n'
##    print pl.getLongestPath().getPathString()
##    print pl.getShortestPath().getPathString()
##    print '\n'
##    print "paths through"
##    for p in pl.getPathsThrough('6'):
##        print p.getPathString()
##    print '\n'
##    paths = pl.getPathsThrough('9', '7', '36')   
##    for p in paths:
##        print p.getPathString()
##    print '\n'
##    print "shortest paths through"
##    for p in pl.getShortestPathsThrough('6'):
##        print p.getPathString()
##    print '\n'
##    for p in pl.getShortestPathsThrough('9', '7', '36'):
##        print p.getPathString()
##    print '\n'        
##    pl.reset()
##    print pl.paths
##    print pl.getNumPaths()
