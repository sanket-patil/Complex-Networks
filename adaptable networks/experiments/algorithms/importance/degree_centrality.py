''' Computes the degree centrality measures. '''

def getDegreeSequence(gr):
    degreesequence = {}
    for nd in gr.getNodes():
        degreesequence[nd.name] = nd.degree
    return degreesequence    

def getDegSeq(gr):
    return [v for v in getDegreeSequence(gr).values()]

def getInDegreeSequence(gr):
    indegreesequence = {}
    for nd in gr.getNodes():
        indegreesequence[nd.name] = nd.indegree
    return indegreesequence

def getInDegSeq(gr):
    return [v for v in getInDegreeSequence(gr).values()]

def getOutDegreeSequence(gr):
    outdegreesequence = {}
    for nd in gr.getNodes():
        outdegreesequence[nd.name] = nd.outdegree
    return outdegreesequence

def getOutDegSeq(gr):
    return [v for v in getOutDegreeSequence(gr).values()]

def getHighestDegree(gr):
    return max([nd.degree for nd in gr.getNodes()])

def getNodeWithMaxDegree(gr):
    ds = getDegreeSequence(gr)
    return max([(ds[k], k) for k in ds])[1]

def getNormalizedHighestDegree(gr):
    ds = getDegSeq(gr)
    return float(max(ds))/float(sum(ds))

def getNormalizedAverageDegree(gr):
    return float(1)/float(gr.getNumNodes())

def getAverageDegree(gr):
    return float(sum([nd.degree for nd in gr.getNodes()]))/float(gr.getNumNodes())

def getHighestInDegree(gr):
    return max([nd.indegree for nd in gr.getNodes()])

def getNormalizedHighestInDegree(gr):
    inds = getInDegSeq(gr)
    return float(max(inds))/float(sum(inds))

def getAverageInDegree(gr):
    return float(sum([nd.indegree for nd in gr.getNodes()]))/float(gr.getNumNodes())

def getNormalizedAverageInDegree(gr):
    return float(1)/float(gr.getNumNodes())

def getHighestOutDegree(gr):
    return max([nd.outdegree for nd in gr.getNodes()])

def getNormalizedHighestOutDegree(gr):
    outds = getOutDegSeq(gr)
    return float(max(outds))/float(sum(outds))

def getAverageOutDegree(gr):
    return float(sum([nd.outdegree for nd in gr.getNodes()]))/float(gr.getNumNodes())

def getNormalizedAverageOutDegree(gr):
    return float(1)/float(gr.getNumNodes())

def getNormalizedDegreeSequence(gr):
    return getDegreeDistribution(gr)

def getDegreeDistribution(gr):
    totaldegree = 0.0
    degreedistribution = {}
    nodes = gr.getNodes()
    for nd in nodes:
        degreedistribution[nd.name] = 0.0
    for nd in nodes:
        degreedistribution[nd.name] = float(nd.degree)
        totaldegree += float(nd.degree)
    for k, v in degreedistribution.items():
        degreedistribution[k] = v/totaldegree
    return degreedistribution

def getInDegreeDistribution(gr):
    totalindegree = 0.0
    indegreedistribution = {}
    nodes = gr.getNodes()
    for nd in nodes:
        indegreedistribution[nd.name] = 0.0
    for nd in gr.getNodes():
        indegreedistribution[nd.name] = float(nd.indegree)
        totalindegree += float(nd.indegree)
    for k, v in indegreedistribution.items():
        indegreedistribution[k] = v/totalindegree
    return indegreedistribution

def getOutDegreeDistribution(gr):
    totaloutdegree = 0.0
    outdegreedistribution = {}
    nd = gr.getNodes()
    for nd in nodes:
        outdegreedistribution[nd.name] = 0.0
    for nd in gr.getNodes():
        outdegreedistribution[nd.name] = float(nd.outdegree)
        totaloutdegree += float(nd.outdegree)
    for k, v in outdegreedistribution.items():
        outdegreedistribution[k] = v/totaloutdegree
    return outdegreedistribution

def getDegreeSkew(gr):
    return float(getHighestDegree(gr)) - getAverageDegree(gr)

def getNormalizedDegreeSkew(gr):
    return getNormalizedHighestDegree(gr) - getNormalizedAverageDegree(gr)

def getInDegreeSkew(gr):
    return float(getHighestInDegree(gr)) - getAverageInDegree(gr)

def getNormalizedInDegreeSkew(gr):
    return getNormalizedHighestInDegree(gr) - getNormalizedAverageInDegree(gr)

def getOutDegreeSkew(gr):
    return float(getHighestOutDegree(gr)) - getAverageOutDegree(gr)

def getNormalizedOutDegreeSkew(gr):
    return getNormalizedHighestOutDegree(gr) - getNormalizedAverageOutDegree(gr)

if __name__ == '__main__':
    print __doc__
    

