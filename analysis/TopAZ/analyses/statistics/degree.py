import algorithms.importance.degree_centrality
import distribution
import entropy

def computeDegreeDistribution(gr):
    numnodes = gr.getNumNodes()
    ds = algorithms.importance.degree_centrality.getDegSeq(gr)    
    return distribution.computeDistribution(ds, 0, numnodes - 1, numnodes)

def computeIndegreeDistribution(gr):
    numnodes = gr.getNumNodes()
    ds = algorithms.importance.degree_centrality.getInDegSeq(gr)    
    return distribution.computeDD(ds, 0, numnodes - 1, numnodes)

def computeIndegreeDistribution(gr):
    numnodes = gr.getNumNodes()
    ds = algorithms.importance.degree_centrality.getOutDegSeq(gr)    
    return distribution.computeDD(ds, 0, numnodes - 1, numnodes)

def computeDegreeCDF(gr):
    numnodes = gr.getNumNodes()
    ds = algorithms.importance.degree_centrality.getDegSeq(gr)
    return distribution.computeCDF(ds, 0, numnodes - 1, numnodes)

def computeIndegreeCDF(gr):
    numnodes = gr.getNumNodes()
    ds = algorithms.importance.degree_centrality.getInDegSeq(gr)
    return distribution.computeCDF(ds, 0, numnodes - 1, numnodes)

def computeOutdegreeCDF(gr):
    numnodes = gr.getNumNodes()
    ds = algorithms.importance.degree_centrality.getOutDegSeq(gr)
    return distribution.computeCDF(ds, 0, numnodes - 1, numnodes)

def computeDegreeDistributionEntropy(gr):
    numnodes = gr.getNumNodes()
    ds = algorithms.importance.degree_centrality.getDegSeq(gr)
    dd = distribution.computeDistribution(ds, 0, numnodes - 1, numnodes)
    return entropy.computeEntropy(dd)

def computeIndegreeDistributionEntropy(gr):
    numnodes = gr.getNumNodes()
    ds = algorithms.importance.degree_centrality.getInDegSeq(gr)
    dd = distribution.computeDistribution(ds, 0, numnodes - 1, numnodes)
    return entropy.computeEntropy(dd)

def computeOutdegreeDistributionEntropy(gr):
    numnodes = gr.getNumNodes()
    ds = algorithms.importance.degree_centrality.getOutDegSeq(gr)
    dd = distribution.computeDistribution(ds, 0, numnodes - 1, numnodes)
    return entropy.computeEntropy(dd)
