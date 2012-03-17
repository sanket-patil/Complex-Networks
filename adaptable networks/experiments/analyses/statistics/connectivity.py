import robustness.robustness_measures
import distribution
import entropy

def computeEdgeConnectivityDistribution(gr):
    econ = robustness.robustness_measures.getConnSeq(gr)
    return distribution.computeDistribution(econ, 0, max(econ), len(econ))

def computeEdgeConnectivityCDF(gr):
    econ = robustness.robustness_measures.getConnSeq(gr)
    return distribution.computeCDF(econ, 1, max(econ), len(econ))

def computeEdgeConnectivityEntropy(gr):
    return entropy.computeEntropy(computeEdgeConnectivityDistribution(gr))

if __name__ == "__main__":
    print 'Statistics related to connectivity.'
