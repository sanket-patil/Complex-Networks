import efficiency.efficiency_measures
import robustness.robustness_measures
import cost.cost_measures
import algorithms.paths.paths
import algorithms.connectivity.connectivity

def computeFitness(gr = None, alpha = 0.0, beta = 0.0, nl = None, el = None, apsp = None, n = 0, e = 0, d = False):
    apsp = apsp
    nl = nl
    el = el
    directed = d
    n = n
    e = e
    alpha = alpha
    if gr:
        directed = gr.directed
        if not algorithms.connectivity.connectivity.isGraphConnected(gr):
            return 0.0
        n = gr.getNumNodes()
        nl = gr.getNodeList()
        el = gr.getEdgeList()
        n = gr.getNumNodes()
        e = gr.getNumEdges()
        apsp = algorithms.paths.paths.getAPSP(gr)
    if not apsp or not nl or not el:
        return -1
    eta = 0.0
    if alpha < 1.0:
        eta = efficiency.efficiency_measures.computeEfficiency(apsp = apsp, n = n, d = directed)
    rho = 0.0
    if alpha > 0.0:
        #rho = robustness.robustness_measures.computeRobustness(gr = gr, apsp = apsp, nl = nl, el = el)
        rho = robustness.robustness_measures.computeRobustness(gr)
    k = 0.0
    if beta > 0.0:
        k = cost.cost_measures.computeCost(e = e, n = n, d = directed)  
    if rho == None or eta == None or k == None:
        return 0.0
    phi = alpha * rho + (1.0 - alpha) * eta - beta * k
    if phi < 0.0:
        phi = 0.0
    return phi

def computeProperties(gr, alpha = 0.0):
    apsp = None
    n = gr.getNumNodes()
    if not gr:
        return None
    if not algorithms.connectivity.connectivity.isGraphConnected(gr):
          return 0.0
    eta = efficiency.efficiency_measures.computeEfficiency(gr)
    app = algorithms.paths.paths.getAllPaths(gr)
    connectivity = {}
    conn = 0
    connv = []
    for src, destdict in app.iteritems():
        for dest, pl in destdict.iteritems():
            if not pl:
                continue            
            conn = pl.getNumPaths()
            connectivity[src + ' ' + dest] = conn
            #print 'ip:', conn
            connv.append(conn)
    print 'minconn', min(connv)
    print 'avcon:', float(avconn)/float(n * (n - 1))
    return

def connectivityBasedRobustness(gr):
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
    #avgconn = float(sum(connv))/float(gr.getNumNodes() * (gr.getNumNodes() - 1))
    #robustness = float(avgconn - 1)/float(gr.getNumNodes() - 2)
    del connv[:]
    #print robustness
    return robustness
            
if __name__ == "__main__":
    print "nothing, right now."
