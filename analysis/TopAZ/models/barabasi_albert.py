import random
import erdos_renyi
import graph.graph
import algorithms.importance.degree_centrality

def createInitialGraph(numnodes = 2, numedges = 1, directed = False, weighted = False):
    initgraph = erdos_renyi.getErdosRenyiGraph(numnodes, numedges, directed, weighted, connected = True)
    return initgraph          
   
def attachNewNodes(gr, start, numnodes, epn):
    for nd1 in range(start + 1, numnodes + 1):
        for k in range(epn):            
            nds = algorithms.importance.degree_centrality.getDegreeSequence(gr)
            while True:
                nd2 = random.choice(preferences(nds))
                if nd2 == str(nd1):
                    continue
                ed = str(nd1) + ' ' + nd2
                if gr.ops.isEdgePresent(ed):
                    continue
                gr.addEdge(ed)
                break
    return

def getBarabasiAlbertGraph(numnodes = 2, epn = 1, initgraphnd = 2, initgraphed = 1, directed = False, weighted = False):
    g = createInitialGraph(initgraphnd, initgraphed, directed, weighted)
    gr = graph.graph.graph(directed = directed, weighted = weighted)
    gr.create(g)
    attachNewNodes(gr, initgraphnd, numnodes, epn)    
    return gr.getEdgeList()

def preferences(nds):
    nodes = ''
    for k, v in nds.items():
        k = str(k) + ' '
        nodes += k * v
    nodes = nodes.split()
    return nodes

if __name__ == '__main__':
    rgs = getWattsStrogatzGraphs(1, 64, 6, beta = 0.0, directed = False)
    for rg in rgs:
        print len(rg)
        print rg
