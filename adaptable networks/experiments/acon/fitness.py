import algorithms.connectivity.connectivity
import algorithms.importance.degree_centrality

def computeFitness(g):
    if g.getNumEdges() > g.getNumNodes() - 1:
        return 0.0
    if not algorithms.connectivity.connectivity.isGraphConnected(g):
        return 1.0/float(g.getNumNodes())
    ds = algorithms.importance.degree_centrality.getDegSeq(g)        
    maxdegree = max(ds)
    numpendants = ds.count(1)
    tcstar = g.getNumNodes() - 1 - maxdegree
    tcline = numpendants - 2
    tcost = max(tcstar, tcline)    
    if tcost > 0:
        return 1.0/float(tcost)
    else:
        return 1.1
    
if __name__ == '__main__':
    print 'Computes fitness.'

