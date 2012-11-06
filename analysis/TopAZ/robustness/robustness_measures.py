import algorithms.importance.degree_centrality
import algorithms.importance.betweenness_centrality
import efficiency.efficiency_measures
import algorithms.connectivity.scc
import random
import math

def computeDRI(gr):
    skew = algorithms.importance.degree_centrality.getNormalizedDegreeSkew(gr)
    minskew = 0.0
    n = float(gr.getNumNodes())
    maxskew = (0.5 * n - 1.0)/n
    DRI = 1 - (skew - minskew)/(maxskew - minskew)
    return DRI

def computeInDRI(gr):
    skew = algorithms.importance.degree_centrality.getNormalizedInDegreeSkew(gr)
    minskew = 0.0
    n = float(gr.getNumNodes())
    maxskew = 0.5 - 1.0/n
    DRI = 1 - (skew - minskew)/(maxskew - minskew)
    return DRI

def computeOutDRI(gr):
    skew = algorithms.importance.degree_centrality.getNormalizedOutegreeSkew(gr)
    minskew = 0.0
    n = float(gr.getNumNodes())
    maxskew = (0.5 * n - 1.0)/n
    DRI = 1 - (skew - minskew)/(maxskew - minskew)
    return DRI

def computeNBRI(gr = None, nl = None, apsp = None):
    skew = algorithms.importance.betweenness_centrality.getNormalizedNodeBetweennessSkew(gr, nl, apsp)
    minskew = 0.0
    n = 0
    if gr:
        n = float(gr.getNumNodes())
    else:
        n = float(len(nl))
    maxskew = 1.0 - 1.0/n
    NBRI = 1 - (skew - minskew)/(maxskew - minskew)
    return NBRI

def getConnectivitySequence(gr = None, app = None):
    if gr:
        app = algorithms.paths.paths.getAllPaths(gr)        
    connectivity = {}
    conn = 0
    for src, destdict in app.iteritems():
        for dest, pl in destdict.iteritems():
            if not pl:
                continue            
            conn = pl.getNumPaths()
            connectivity[src + ' ' + dest] = conn
    return connectivity

def worstcaseEdgeConnectivityRI(gr):
    app = algorithms.paths.paths.getAllPaths(gr)
    connv = []
    for src, destdict in app.iteritems():
        for dest, pl in destdict.iteritems():
            if not pl:
                return 0.0
            conn = pl.getNumPaths()
            if conn < 2:
                return 0.0
            connv.append(conn)
    robustness = float(min(connv) - 1)/float(gr.getNumNodes() - 2)
    del connv[:]
    return robustness

def avgcaseEdgeConnectivityRI(gr):
    app = algorithms.paths.paths.getAllPaths(gr)
    connv = []
    for src, destdict in app.iteritems():
        for dest, pl in destdict.iteritems():
            if not pl:
                return 0.0
            conn = pl.getNumPaths()
            connv.append(conn)    
    avgconn = float(sum(connv))/float(gr.getNumNodes() * (gr.getNumNodes() - 1))
    robustness = float(avgconn - 1)/float(gr.getNumNodes() - 2)
    del connv[:]
    return robustness

def getAvgVertexCutsetSize(gr):
    el = gr.getEdgeList()
    for i in range(100):
        pass        

def getAvgEdgeCutsetSize(gr):
    pass

def getConnSeq(gr = None, app = None):
    return [v for v in getConnectivitySequence(gr = gr, app = app).values()]

def nbBasedEfficiencyDrop(gr):
    el = gr.getEdgeList()
    eff1 = efficiency.efficiency_measures.computeEfficiency(gr)
    centralnode = algorithms.importance.betweenness_centrality.getNodeWithMaxBetweenness(gr = gr)
    gr.removeNode(centralnode)
    eff2 = efficiency.efficiency_measures.computeEfficiency(gr)
    effdrop = eff1 - eff2
    gr.reset()
    gr.create(el)
    return effdrop

def ebBasedEfficiencyDrop(gr):
    el = gr.getEdgeList()
    eff1 = efficiency.efficiency_measures.computeEfficiency(gr)
    centraledge = algorithms.importance.betweenness_centrality.getEdgeWithMaxBetweenness(gr = gr)
    gr.removeEdge(centraledge)
    eff2 = efficiency.efficiency_measures.computeEfficiency(gr)
    effdrop = eff1 - eff2
    gr.reset()
    gr.create(el)
    return effdrop

def degreeBasedEfficiencyDrop(gr):
    el = gr.getEdgeList()
    eff1 = efficiency.efficiency_measures.computeEfficiency(gr)
    centralnode = algorithms.importance.degree_centrality.getNodeWithMaxDegree(gr = gr)
    gr.removeNode(centralnode)
    eff2 = efficiency.efficiency_measures.computeEfficiency(gr)
    effdrop = eff1 - eff2
    gr.reset()
    gr.create(el)
    return effdrop

def computeNBEDRI(gr):
    ed = nbBasedEfficiencyDrop(gr)
    return max(1.0 - ed, 0.0)

def computeEBEDRI(gr):
    ed = ebBasedEfficiencyDrop(gr)
    return max(1.0 - ed, 0.0)

def computeDegreeEDRI(gr):
    ed = degreeBasedEfficiencyDrop(gr)
    return max(1.0 - ed, 0.0)

def randomNodeEfficiencyDrop(gr):
    el = gr.getEdgeList()
    eff1 = efficiency.efficiency_measures.computeEfficiency(gr)
    nd = random.choice(gr.getNodeList())
    gr.removeNode(nd)
    eff2 = efficiency.efficiency_measures.computeEfficiency(gr)
    effdrop = eff1 - eff2
    gr.reset()
    gr.create(el)
    return effdrop

def computeRNEDRI(gr):
    ed = randomNodeEfficiencyDrop(gr)
    return max(1.0 - ed, 0.0)

def randomEdgeEfficiencyDrop(gr):
    el = gr.getEdgeList()
    eff1 = efficiency.efficiency_measures.computeEfficiency(gr)
    ed = random.choice(gr.getEdgeList())
    gr.removeEdge(ed)
    eff2 = efficiency.efficiency_measures.computeEfficiency(gr)
    effdrop = eff1 - eff2
    gr.reset()
    gr.create(el)
    return effdrop

def computeREEDRI(gr):
    ed = randomEdgeEfficiencyDrop(gr)
    return max(1.0 - ed, 0.0)

def nbBasedFNRI(gr):
    if not algorithms.connectivity.connectivity.isGraphConnected(gr):
        return 0.0
    el = gr.getEdgeList()
    n = gr.getNumNodes()
    centralnode = algorithms.importance.betweenness_centrality.getNodeWithMaxBetweenness(gr = gr)
    gr.removeNode(centralnode)    
    nwsize = float(algorithms.connectivity.scc.sizeOfLargestSCC(gr))/float(n - 1)    
    res = 1.0 - nwsize
    worstres = 1.0 - (1.0/float(n - 1))
    fnrob = 1.0 - (res/worstres)
    gr.reset()
    gr.create(el)
    return fnrob

def ebBasedFNRI(gr):
    if not algorithms.connectivity.connectivity.isGraphConnected(gr):
        return 0.0
    el = gr.getEdgeList()
    n = gr.getNumNodes()
    centraledge = algorithms.importance.betweenness_centrality.getEdgeWithMaxBetweenness(gr = gr)
    gr.removeEdge(centraledge)    
    nwsize = float(algorithms.connectivity.scc.sizeOfLargestSCC(gr))/float(n)    
    res = 1.0 - nwsize
    worstres = 1.0 - float(math.ceil(n/2))/float(n)
    fnrob = 1.0 - (res/worstres)
    gr.reset()
    gr.create(el)
    return fnrob

def degreeBasedFNRI(gr):
    if not algorithms.connectivity.connectivity.isGraphConnected(gr):
        return 0.0
    el = gr.getEdgeList()
    n = gr.getNumNodes()
    centralnode = algorithms.importance.degree_centrality.getNodeWithMaxDegree(gr)
    gr.removeNode(centralnode)
    nwsize = float(algorithms.connectivity.scc.sizeOfLargestSCC(gr))/float(n - 1)
    res = 1.0 - nwsize
    worstres = 1.0 - (1.0/float(n - 1))
    fnrob = 1.0 - (res/worstres)
    gr.reset()
    gr.create(el)
    return fnrob

def RNFNRI(gr):
    if not algorithms.connectivity.connectivity.isGraphConnected(gr):
        return 0.0
    el = gr.getEdgeList()
    n = gr.getNumNodes()
    nd = random.choice(gr.getNodeList())
    gr.removeNode(nd)
    nwsize = float(algorithms.connectivity.scc.sizeOfLargestSCC(gr))/float(n - 1)
    res = 1.0 - nwsize
    worstres = 1.0 - (1.0/float(n - 1))
    fnrob = 1.0 - (res/worstres)
    gr.reset()
    gr.create(el)
    return fnrob

def REFNRI(gr):
    if not algorithms.connectivity.connectivity.isGraphConnected(gr):
        return 0.0
    el = gr.getEdgeList()
    n = gr.getNumNodes()
    ed = random.choice(gr.getEdgeList())
    gr.removeEdge(ed)
    nwsize = float(algorithms.connectivity.scc.sizeOfLargestSCC(gr))/float(n)
    res = 1.0 - nwsize
    worstres = 1.0 - float(math.ceil(n/2))/float(n)
    fnrob = 1.0 - (res/worstres)
    gr.reset()
    gr.create(el)
    return fnrob

def computeRobustness(gr = None, nl = None, el = None, apsp = None):
    #return computeDRI(gr)
    #return computeNBRI(gr, nl, apsp)
    return degreeBasedFNRI(gr)
    #return RNFNRI(gr)
    #return nbBasedFNRI(gr) 
