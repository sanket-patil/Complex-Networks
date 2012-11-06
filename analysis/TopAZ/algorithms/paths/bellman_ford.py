''' Single Source Shortest Paths: Bellman-Ford Algorithm '''

import sys
import pathlist
import path

def bellmanFord(gr, s, sponly = True, allsp = False):
    dist = {}
    paths = {}
    for u in gr.getNodeList():
        dist[u] = sys.maxint/2
        paths[u] = pathlist.pathlist()
    dist[s] = 0
    paths[s].addPath(path.path([s], weight = dist[s]))
    nodes = gr.getNodes()
    edges = gr.getEdges()    
    for i in range(gr.getNumNodes()):
        for ed in edges:
            u = ed.head
            v = ed.tail
            if sponly == False:
                altPaths(v, paths[u], paths[v])
                if not gr.directed:
                    u = ed.tail
                    v = ed.head
                    altPaths(v, paths[u], paths[v])
            else:                
                alt = dist[u] + ed.weight    
                if alt < dist[v]:
                    relaxEdge(alt, v, dist, paths[u], paths[v])
                if allsp:
                    if alt == dist[v]:
                        altPaths(v, paths[u], paths[v])
                if not gr.directed:
                    u = ed.tail
                    v = ed.head
                    alt = dist[u] + ed.weight
                    if alt < dist[v]:
                        relaxEdge(alt, v, dist, paths[u], paths[v])
                    if allsp:
                        if alt == dist[v]:
                            altPaths(v, paths[u], paths[v])
    paths[s].reset()
    del paths[s]
    if sponly:
        for ed in edges:
            u = ed.head
            v = ed.tail
            if not gr.directed:
                if dist[v] > dist[u] + ed.weight and dist[u] > dist[v] + ed.weight:
                    print "Error: Graph contains a negative cycle!"
            else:
                if dist[v] > dist[u] + ed.weight:
                    print ed.name
                    print "Error: Graph contains a negative cycle!"
    return paths

def relaxEdge(alt, v, dist, pathsu, pathsv):
    if alt < dist[v]:
        dist[v] = alt                
        pathsv.reset()
        for p in pathsu.getPathList():
            q = []
            for n in p.getPathString().split():
                q.append(n)
            q.append(v)
            pathsv.addPath(path.path(q, weight = dist[v]))    
    return

##def altPaths(v, pathsu, pathsv):
##    for p in pathsu.getPathList():
##        if p.isNodeInPath(v):
##            continue
##        q = []
##        for n in p.getPathString().split():
##            q.append(n)
##        q.append(v)
##        q = path.path(q, weight = p.getPathWeight())
##        if not pathsv.isPathInList(q):
##            pathsv.addPath(q)
##    return

def altPaths(v, pathsu, pathsv):
    for p in pathsu.getPathList():
        if p.isNodeInPath(v):
            continue
        q = []
        for n in p.getPathString().split():
            q.append(n)
        q.append(v)
        q = path.path(q, weight = p.getPathWeight())
        if not pathsv.isPathInList(q) and pathsv.isPathEdgeIndependent(q):
            pathsv.addPath(q)
    return
    
def getShortestPathsFrom(gr, s):
    pass

def getShortestPathBetween(gr, src, dest):
    pass

def getShortestPathsBetween(gr, src, dest):
    pass

if __name__ == "__main__":
    print __doc__
