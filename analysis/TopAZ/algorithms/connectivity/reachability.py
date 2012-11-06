''' Computes the basic reachability properties. Algorithms implemented include: (1) BFS (2) DFS '''

def getBFSTree(gr, nd = None):
    if not nd:
        nd = gr.getNodes()[0]
    bfsTree = []    
    bfsqueue = []
    search(nd, bfsqueue)
    while bfsqueue:
        ed = bfsqueue.pop(0)
        w = ed.split()[1]
        w = gr.getNode(w)
        if not w.visited:
            bfsTree.append(ed)
            search(w, bfsqueue)            
    gr.resetNodeVisitedFlags()
    return bfsTree

def getNodesReachableFrom(gr, nd):
    return getBFSTree(gr, nd)

def getNodesNotReachableFrom(gr, nd):
    bfsTree = getBFSTree(gr, nd)
    return [n.name for n in gr.getNodes if n.name not in bfsTree]

def getDFSTree(gr, nd = None):
    if not nd:
        nd = gr.getNodes()[0]
    dfsTree = []
    dfsstack = []
    search(nd, dfsstack)
    while dfsstack:
        ed = dfsstack.pop()
        w = gr.getNode(ed.split()[1])
        if not w.visited:
            dfsTree.append(ed)
            search(w, dfsstack)         
    gr.resetNodeVisitedFlags()
    return dfsTree    

def DFS(gr, stack, v):
    v = gr.getNode(v)
    v.visited = True
    for w in v.getNeighbours():
        w = gr.getNode(w)
        if not w.visited:
            DFS(gr, stack, w.name)
            stack.append(w.name)
    return

def search(v, l):
    v.visited = True
    for w in v.getNeighbours():
        l.append(v.name + " " + w)
    return
    
if __name__ == '__main__':
    print __doc__
    

