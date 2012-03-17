import sys
import breeder
import random_graphs
import graph.graph
import algorithms.connectivity.connectivity
import algorithms.importance.degree_centrality

def computeBestAcon(argv):
    n = int(argv[1])
    rgs = random_graphs.getRandomGraphs(1000, n, n - 1)
    tcosts = computeTransitionCosts(rgs, n)
    for tcost in tcosts:
        print tcost
    print len(tcosts)
    return

def computeTransitionCosts(rgs, n):
    tcosts = []
    g = graph.graph.graph()    
    for rg in rgs:
        g.create(rg, n)
        if not algorithms.connectivity.connectivity.isGraphConnected(g):
            g.reset()
            continue
        ds = algorithms.importance.degree_centrality.getDegSeq(g)        
        maxdegree = max(ds)
        numpendants = ds.count(1)
        tcstar = n - 1 - maxdegree
        tcline = numpendants - 2
        tcost = []
        tcost.append(rg)
        tcost.append(tcstar)
        tcost.append(tcline)
        tcosts.append(tcost)
        g.reset()
    return tcosts
        
if __name__ == '__main__':
    computeBestAcon(sys.argv)

