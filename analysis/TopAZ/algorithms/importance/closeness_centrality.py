''' Computes the closeness centrality measures. '''
import algorithms.paths.paths

def getClosenessSequence(gr = None, nl = None, apsp = None):
    plist = apsp
    nodes = nl
    closeness = {}
    if gr:
        nodes = gr.getNodeList()
        plist = algorithms.paths.paths.getAPSP(gr)
    if not plist or not nodes:
        return None
    for v in nodes:
        closeness[v] = 0.0
    for v in closeness.keys():
        apl = 0.0
        numpaths = 0
        for p in plist[v].getPathList():
            apl += float(p.getPathLength())
            numpaths += 1
        if apl and numpaths:
            closeness[v] = apl/float(numpaths)
    return closeness

def getClosenessVectors(gr = None, nl = None, apsp = None):
    plist = apsp
    nodes = nl
    closenessv = {}
    if gr:
        nodes = gr.getNodeList()
        plist = algorithms.paths.paths.getAPSP(gr)
    if not plist or not nodes:
        return None
    for v in nodes:
        closenessv[v] = []
    for v in closenessv.keys():
        for p in plist[v].getPathList():
            closenessv[v].append(p.getPathLength())
    return closenessv

def getCloseSeq(gr = None, nl = None, apsp = None):
    return [v for v in getClosenessSequence(gr, nl, apsp).values()]

def getClosenessDistribution(gr = None, nl = None, apsp = None):
    closeness = getClosenessSequence(gr, nl, apsp)
    total = sum([v for v in closeness.values()])
    for v in closeness.keys():
        closeness[v] /= total
    return closeness

def getCloseDist(gr = None, nl = None, apsp = None):
    return [v for v in getClosenessDistribution(gr, nl, apsp).values()]

def getHighestClosenss(gr = None, nl = None, apsp = None):    
    return max(getCloseSeq(gr, nl, apsp))

def getAverageCloseness(gr = None, nl = None, apsp = None):
    if gr:
        return sum(getCloseSeq(gr))/float(gr.getNumNodes())
    if nl and apsp:
        return sum(getCloseSeq(gr, nl, apsp))/float(len(nl))
    return -1

def getNormalizedHighestCloseness(gr = None, nl = None, apsp = None):
    return max(getCloseDist(gr, nl, apsp))

def getNormalizedAverageCloseness(gr = None, nl = None, apsp = None):
    if gr:
        return 1.0/float(gr.getNumNodes())
    if nl and apsp:
        return 1.0/float(len(nl))

def getClosenessSkew(gr = None, nl = None, apsp = None):
    clseq = getCloseSeq(gr, nl, apsp)
    maxcl = max(clseq)
    n = 0
    if gr:
        n = float(gr.getNumNodes())
    else:
        n = float(len(nl))
    avcl = sum(clseq)/n
    return maxcl - avcl

def getNormalizedClosenessSkew(gr = None, nl = None, apsp = None):
    cldist = getCloseDist(gr, nl, apsp)
    maxcl = max(cldist)
    n = 0
    if gr:
        n = float(gr.getNumNodes())
    else:
        n = float(len(nl))
    avcl = 1.0/n
    return maxcl - avcl

def getNodeCloseness(gr, nd):
    pass

if __name__ == '__main__':
    print __doc__
    

