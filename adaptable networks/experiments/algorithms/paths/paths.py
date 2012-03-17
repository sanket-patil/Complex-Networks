''' Single Source Shortest Paths: Dijkstra's Algorithm '''
import sys
import pathlist
import bellman_ford
import bfsbased

def getAPSP(gr, allsp = False):
    apsp = {}
    nodes = gr.getNodeList()
    for nd in nodes:
        apsp[nd] = pathlist.pathlist()
    paths = None
    if not gr.weighted:
        for nd in nodes:
            paths = bfsbased.bfsBasedShortestPaths(gr, nd, allsp = False)
            for v in paths.values():
                for p in v.getPathList():
                    apsp[nd].addPath(p)
    else:
        for nd in nodes:
            paths = bellman_ford.bellmanFord(gr, nd, allsp = False)
            for v in paths.values():
                for p in v.getPathList():
                    apsp[nd].addPath(p)
        #apsp[nd] = paths

    return apsp

def getAllPaths(gr):
    app = {}
    nodes = gr.getNodeList()
    #for nd in nodes:
    #    app[nd] = pathlist.pathlist()
    for nd in nodes:
        paths = bellman_ford.bellmanFord(gr, nd, sponly = False)
     #   for v in paths.values():
     #       for p in v.getPathList():
     #           app[nd].addPath(p)
        app[nd] = paths
    return app

def getAPSPMatrix(gr):
    apsp = getAPSP(gr)
    apspmatrix = []
    nodes = gr.getNodeList()
    for nd in nodes:
        pl = apsp[nd].getPathList()
        for p in pl:
            entry = 'src: ' + nd + '\tdest: ' + p.getDestination() + '\tlen: ' + str(p.getPathLength()) + '\tpath: ' + p.getPathString()
            apspmatrix.append(entry)
    return apspmatrix

if __name__ == "__main__":
    print __doc__
