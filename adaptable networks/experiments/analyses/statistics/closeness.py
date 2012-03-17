import algorithms.importance.closeness_centrality
import distribution
import entropy

def computeClosenessDistribution(gr):
    pass

def computeClosenessCDF(gr):
    pass

def computeClosenessEntropy(gr):
    pass

def computePLDistribution(gr, interval):
    clsv = algorithms.importance.closeness_centrality.getClosenessVectors(gr)
    cls = []
    for v in clsv.values():
        cls.extend(v)
    print min(cls)
    return distribution.computeDistribution(cls, 0, max(cls), interval, len(cls))

def computePLCDF(gr, interval):
    clsv = algorithms.importance.closeness_centrality.getClosenessVectors(gr)
    cls = []
    for v in clsv.values():
        cls.extend(v)
    return distribution.computeCDF(cls, 0, max(cls), interval, len(cls))

def computePLEntropy(gr, interval):
    return entropy.computeEntropy(computePLDistribution(gr, interval))

if __name__ == "__main__":
    print 'Statistics related to betweenness.'
