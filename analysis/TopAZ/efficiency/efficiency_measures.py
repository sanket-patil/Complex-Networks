import algorithms.connectivity.connectivity
import algorithms.paths.paths
import random

def getAPL(gr):
    pass

def getDiameter(gr = None, apsp = None):
    apsp = apsp
    if gr:
        if not algorithms.connectivity.connectivity.isGraphConnected(gr):
            return gr.getNumNodes()
        apsp = algorithms.paths.paths.getAPSP(gr)
    if not apsp:
        return -1
    k = apsp.keys()[0]
    diapath = apsp[k].getPath()
    diameter = diapath.getPathLength()
    for v in apsp.values():
        lp = v.getLongestPath()
        if not lp:
            return -1
        lpl = lp.getPathLength()
        if lpl > diameter:
            diameter = lpl
            diapath = lp    
    return diameter

def getAPL(gr = None, apsp = None):
    apl = 0.0
    apsp = apsp
    if gr:
        if not algorithms.connectivity.connectivity.isGraphConnected(gr):
            return gr.getNumNodes()
        apsp = algorithms.paths.paths.getAPSP(gr)
    if not apsp:
        return -1
    numpaths = 0.0
    for v in apsp.values():
        for p in v.getPathList():
            apl += float(p.getPathLength())
        numpaths += v.getNumPaths()
    apl /= numpaths
    return apl 

def getEccentricityDistribution(gr = None, nl = None, apsp = None):
    eccdist = {}
    nodes = nl
    apsp = apsp
    if gr:
        if not algorithms.connectivity.connectivity.isGraphConnected(gr):
            return gr.getNumNodes()
        apsp = algorithms.paths.paths.getAPSP(gr)
        nodes = gr.getNodeList()    
    if not apsp or not nodes:
        return None
    for v in nodes:
        eccdist[v] = 0.0
    dia = 0.0
    for v in eccdist.keys():
        lp = apsp[v].getLongestPath()
        if not lp:
            continue
        eccdist[v] = float(lp.getPathLength())
        if eccdist[v] > dia:
            dia = eccdist[v]
    for v in eccdist.keys():
        eccdist[v] /= dia
    return eccdist

def getNormalizedEcc(gr = None, nl = None, apsp = None):
    return [v for v in getEccentricityDistribution(nl = nl, apsp = apsp).values()]

def getEccentricitySequence(gr = None, nl = None, apsp = None):
    eccseq = {}
    nodes = nl
    apsp = apsp
    if gr:
        if not algorithms.connectivity.connectivity.isGraphConnected(gr):
            return gr.getNumNodes()
        apsp = algorithms.paths.paths.getAPSP(gr)
        nodes = gr.getNodeList()    
    if not apsp or not nodes:
        return None
    for v in nodes:
        eccseq[v] = 0
    for v in eccseq.keys():
        lp = apsp[v].getLongestPath()
        if not lp:
            continue
        eccseq[v] = lp.getPathLength()
    return eccseq

def getRadius(gr = None, nl = None, apsp = None):    
    es = getEccentricitySequence(gr, nl, apsp)
    ecc = [v for v in es.values()]
    return min(ecc)

def getRadialNodes(gr = None, nl = None, apsp = None):
    es = getEccentricitySequence(gr, nl, apsp)
    radius = min([v for v in es.values()])
    radialnodes = []
    for k, v in es.items():
        if v == radius:
            radialnodes.append(k)
    return radialnodes

def getNumRadii(gr = None, nl = None, apsp = None):
    ed = getEccentricityDistribution(gr, nl, apsp)
    ed = [v for v in ed.values()]
    radius = min(ed)
    numradii = 0
    for r in ed:
         if r == radius:
             numradii += 1
    return numradii     

def getPeripheralNodes(gr = None, nl = None, apsp = None):
    es = getEccentricitySequence(gr, nl, apsp)
    eccentricity = max([v for v in es.values()])
    peripheralnodes = []
    for k, v in es.items():
        if v == eccentricity:
            peripheralnodes.append(k)
    return peripheralnodes

def computeEfficiency(gr = None, d = False, n = 0, apsp = None):    
    #conf = open('config.txt')
    #conf = conf.read()
    #measure = conf.split('\n')[0]
    #if measure == 'diameter':
    #
    #return diaBasedEff(gr, d, n, apsp)
    #elif measure == 'apl':
    return aplBasedEff(gr, d, n, apsp)    

def diaBasedEff(gr = None, d = False, n = 0, apsp = None):
    apsp = apsp
    n = n
    directed = d
    if gr:
        diameter = getDiameter(gr)
        if diameter == -1:
            return -1
        n = gr.getNumNodes()
        directed = gr.directed
        eff = float(1) - (float(diameter - 1)/float(n - 2))
        return eff
    if apsp and n > 0:
        diameter = getDiameter(apsp = apsp)
        if diameter == -1:
            return -1
        eff = float(1) - (float(diameter - 1)/float(n - 2))
        return eff
    return -1

def aplBasedEff(gr = None, d = False, n = 0, apsp = None):
    apsp = apsp
    n = n
    directed = d
    if gr:
        apl = getAPL(gr)
        if apl == -1:
            return -1
        n = gr.getNumNodes()
        directed = gr.directed
        if not directed:
            eff = float(1) - 3 * (float(apl - 1)/float(n - 2))
        else:
            eff = float(1) - 2 * (float(apl - 1)/float(n - 2))
        return eff
    if apsp and n > 0:
        apl = getAPL(apsp = apsp)
        if apl == -1:
            return -1
        if not directed:
            eff = float(1) - 3 * (float(apl - 1)/float(n - 2))
        else:
           eff = float(1) - 2 * (float(apl - 1)/float(n - 2))
        return eff
    return -1
