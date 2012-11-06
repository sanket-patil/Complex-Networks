import algorithms.importance.betweenness_centrality
import distribution
import entropy

def computeNodeBetweennessDistribution(gr):
    numnodes = gr.getNumNodes()
    nbs = algorithms.importance.betweenness_centrality.getNodeBetnSeq(gr)
    return distribution.computeDistribution(nbs, 0, numnodes * (numnodes - 1), numnodes)

def computeNodeBetweennessCDF(gr):
    numnodes = gr.getNumNodes()
    nbs = algorithms.importance.betweenness_centrality.getNodeBetnSeq(gr)
    return distribution.computeCDF(nbs, 0, numnodes * (numnodes - 1), numnodes)

def computeNodeBetweennessEntropy(gr):
    numnodes = gr.getNumNodes()
    nbs = algorithms.importance.betweenness_centrality.getNodeBetnSeq(gr)
    nbd = distribution.computeDistribution(nbs, 0, numnodes * (numnodes - 1), numnodes)
    return entropy.computeEntropy(nbd)

def computeEdgeBetweennessDistribution(gr):
    numedges = gr.getNumEdges()
    numnodes = gr.getNumNodes()
    ebs = algorithms.importance.betweenness_centrality.getEdgeBetnSeq(gr)    
    return distribution.computeDistribution(ebs, 0, numnodes * (numnodes - 1), numedges)

def computeEdgeBetweennessCDF(gr):
    numedges = gr.getNumEdges()    
    numnodes = gr.getNumNodes()
    ebs = algorithms.importance.betweenness_centrality.getEdgeBetnSeq(gr)
    return distribution.computeCDF(ebs, 0, numnodes * (numnodes - 1), numedges)

def computeEdgeBetweennessEntropy(gr):
    numedges = gr.getNumEdges()
    numnodes = gr.getNumNodes()
    ebs = algorithms.importance.betweenness_centrality.getEdgeBetnSeq(gr)
    ebd = distribution.computeDistribution(ebs, 0, numnodes * (numnodes - 1), numedges)
    return entropy.computeEntropy(ebd)


if __name__ == "__main__":
    print 'Statistics related to betweenness.'
