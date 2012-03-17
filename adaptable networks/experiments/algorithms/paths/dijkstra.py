''' Single Source Shortest Paths: Dijkstra's Algorithm '''
import sys
import pathlist

def dijkstra(gr, s):
    dist = {}
    paths = {}
    for u in gr.getNodes():
        dist[u.name] = sys.maxint
        paths[u.name] = pathlist.pathlist()
    #dist[s] = 0
    nodeQ = gr.getNodes()
    nodeQ.remove(gr.getNode(s))
    print nodeQ
    while nodeQ:
        #nd = min(dist,key = lambda m: dist.get(m))
        nd = getNodeWithMinDist(dist)
        print nd
        u = gr.getNode(nd)
        print u
        nodeQ.remove(u)
        for v in u.getNeighbours():
            alt = dist[u.name] + gr.operations.getEdgeBetween(u.name, v).weight
            if alt < dist[v]:
                dist[v] = alt
                if not paths[u].getPaths():
                    p = path.path([v])
                    paths[v].addPath(p)
                for p in paths[u].getPaths():
                    q = path.path(p.append(v))
                    paths[v] = paths[v].addPath(q)
            elif alt == dist[v]:
                p = path.path(paths[u.name].append(v))
                paths[v] = paths[v].addPath(p)

    return dist                

def getNodeWithMinDist(dist):
    nd = ''
    d = sys.maxint
    for k, v in dist.iteritems():
        print k, v
        if v <= d:
            d = v
            nd = k
    return nd

def getShortestPathsFrom(gr, nd):
    pass

def getShortestPathBetween(gr, nd1, nd2):
    pass

def getShortestPathsBetween(gr, nd1, nd2):
    pass

if __name__ == "__main__":
    print __doc__
