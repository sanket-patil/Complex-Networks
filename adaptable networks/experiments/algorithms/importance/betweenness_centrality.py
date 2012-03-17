''' Computes the betweenness centrality measures. '''
import algorithms.paths.paths

def getNodeBetweennessSequence(gr = None, nl = None, apsp = None):
    betweenness = {}
    plist = apsp
    nodes = nl
    if gr:
        nodes = gr.getNodeList()
        plist = algorithms.paths.paths.getAPSP(gr, allsp = True)
    elif not nodes or not plist:
        return None        
    for v in nodes:
            betweenness[v] = 0.0
    for v in betweenness.keys():
        for s in betweenness.keys():
            if s == v:
                continue
            for t in betweenness.keys():
                if t == v or t == s:
                    continue
                froms = plist[s]
                thru = float(froms.getNumShortestPathsThroughNode(v, s, t))
                betn = float(froms.getNumShortestPathsBetween(s, t))
                incr = 0.0
                if not betn == 0.0:
                    incr = thru/betn
                betweenness[v] += incr   
    return betweenness

def getNodeBetnSeq(gr = None, nl = None, apsp = None):
    nbseq = getNodeBetweennessSequence(gr, nl, apsp)
    return [v for v in nbseq.values()]

def getNodeBetweennessDistribution(gr = None, nl = None, apsp = None):
    betweenness = getNodeBetweennessSequence(gr, nl, apsp)
    total = sum([v for v in betweenness.values()])
    if total:
        for k, v in betweenness.items():
            betweenness[k] = v/total    
    return betweenness                

def getNodeBetnDist(gr = None, nl = None, apsp = None):
    nbdist = getNodeBetweennessDistribution(gr, nl, apsp)
    return [v for v in nbdist.values()]

def getNodeBetweenness(gr, nd):    
    betweenness = 0.0
    total = 0.0
    plist = algorithms.paths.apsp.getAPSP(gr)
    nodes = [v.name for v in gr.getNodes()]
    for s in nodes and s is not v:
        for t in nodes and t is not v and t is not s:
            betweenness += plist.getNumShortestPathsThroughNode(v, s, t)/plist.getNumShortestPathsBetween(s, t)
            total += betweenness    
    betweenness[k] = v/total        
    return betweenness

def getHighestNodeBetweenness(gr = None, nl = None, apsp = None):
    return max(getNodeBetnSeq(gr, nl, apsp))

def getNodeWithMaxBetweenness(gr = None, nl = None, apsp = None):
    nbseq = getNodeBetweennessSequence(gr, nl, apsp)
    return max([(nbseq[k],k) for k in nbseq])[1]

def getAverageNodeBetweenness(gr = None, nl = None, apsp = None):
    if gr:
        return sum(getNodeBetnSeq(gr))/float(gr.getNumNodes())
    if nl and apsp:
        return sum(getNodeBetnSeq(gr, nl, apsp))/float(len(nl))
    return -1

def getNormalizedHighestNodeBetweenness(gr = None, nl = None, apsp = None):
    return max(getNodeBetnDist(gr, nl, apsp))

def getNormalizedAverageNodeBetweenness(gr = None, nl = None, apsp = None):
    if gr:
        return 1.0/float(gr.getNumNodes())
    if nl and apsp:
        return 1.0/float(len(nl))
    return -1

def getNodeBetweennessSkew(gr = None, nl = None, apsp = None):
    nbseq = getNodeBetnSeq(gr, nl, apsp)
    maxbetn = max(nbseq)
    n = 0
    if gr:
        n = float(gr.getNumNodes())
    else:
        n = float(len(nl))
    avbetn = sum(nbseq)/n
    return maxbetn - avbetn

def getNormalizedNodeBetweennessSkew(gr = None, nl = None, apsp = None):
    nbdist = getNodeBetnDist(gr, nl, apsp)
    maxbetn = max(nbdist)
    n = 0
    if gr:
        n = float(gr.getNumNodes())
    else:
        n = float(len(nl))
    avbetn = 1.0/n
    return maxbetn - avbetn

def getEdgeBetweennessSequence(gr = None, nl = None, el = None, apsp = None):
    betweenness = {}
    plist = apsp
    edges = el
    nodes = nl
    if gr:
        nodes = gr.getNodeList()
        edges = gr.getEdgeList()
        plist = algorithms.paths.paths.getAPSP(gr, allsp = True)
    elif not edges or not nodes or not plist:
        return None        
    for ed in edges:
        betweenness[ed] = 0.0
    for s in nodes:
        for t in nodes:
            if s == t:
                continue
            for ed in betweenness.keys():
                froms = plist[s]
                thru = float(froms.getNumShortestPathsThroughEdge(ed, s, t))
                betn = float(froms.getNumShortestPathsBetween(s, t))
                incr = 0
                if not thru == 0.0 and not betn == 0.0:
                    incr = thru/betn
                betweenness[ed] += incr    
    return betweenness

def getEdgeBetnSeq(gr = None, nl = None, el = None, apsp = None):
    edbseq = getEdgeBetweennessSequence(gr, nl, el, apsp)
    return [v for v in edbseq.values()]

def getEdgeBetweennessDistribution(gr = None, nl = None, el = None, apsp = None):
    betweenness = getEdgeBetweennessSequence(gr, nl, el, apsp)
    total = sum([v for v in betweenness.values()])
    for k, v in betweenness.items():
        betweenness[k] = v/total
    return betweenness                

def getEdgeBetnDist(gr = None, nl = None, el = None, apsp = None):
    edbdist = getEdgeBetweennessDistribution(gr, nl, el, apsp)
    return [v for v in edbdist.values()]

def getEdgeBetweenness(gr, ed):    
    pass

def getHighestEdgeBetweenness(gr = None, nl = None, el = None, apsp = None):
    return max(getEdgeBetnSeq(gr, nl, el, apsp))

def getEdgeWithMaxBetweenness(gr = None, nl = None, el = None, apsp = None):
    ebseq = getEdgeBetweennessSequence(gr, nl, el, apsp)
    return max([(ebseq[k],k) for k in ebseq])[1]

def getAverageEdgeBetweenness(gr = None, nl = None, el = None, apsp = None):
    if gr:
        return sum(getEdgeBetnSeq(gr))/float(gr.getNumEdges())
    if nl and el and apsp:
        return sum(getEdgeBetnSeq(gr, nl, el, apsp))/float(len(el))
    return -1

def getNormalizedHighestEdgeBetweenness(gr = None, nl = None, el = None, apsp = None):
    return max(getEdgeBetnDist(gr, nl, el, apsp))

def getNormalizedAverageEdgeBetweenness(gr = None, nl = None, el = None, apsp = None):
    if gr:
        return 1.0/float(gr.getNumEdges())
    if nl and el and apsp:
        return 1.0/float(len(el))
    return -1

def getEdgeBetweennessSkew(gr = None, nl = None, el = None, apsp = None):
    edbseq = getEdgeBetnSeq(gr, nl, el, apsp)
    maxbetn = max(edbseq)
    ne = 0
    if gr:
        ne = float(gr.getNumEdges())
    else:
        ne = float(len(el))
    avbetn = sum(edbseq)/ne
    return maxbetn - avbetn

def getNormalizedEdgeBetweennessSkew(gr = None, nl = None, el = None, apsp = None):
    edbdist = getEdgeBetnDist(gr, nl, el, apsp)
    maxbetn = max(edbdist)
    ne = 0
    if gr:
        ne = float(gr.getNumEdges())
    else:
        ne = float(len(el))
    avbetn = 1.0/ne
    return maxbetn - avbetn

if __name__ == '__main__':
    print __doc__
    

