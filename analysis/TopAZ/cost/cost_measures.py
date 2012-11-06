
def computeCost(gr = None, n = 0, e = 0, d = False):
    if gr:
        if gr.weighted:
            return computeWeightedCost(gr)
    n = n
    e = e
    directed = d
    k = 0.0
    if gr:
        n = gr.getNumNodes()
        e = gr.getNumEdges()
        directed = gr.directed        
    if n == 0 or e == 0:
        return k
    if not directed:
        emin = n - 1
        emax = n * (n - 1)/2
        k = float(e - emin)/float(emax - emin)
        return k
    emin = n    
    emax = n * (n - 1)
    if emax == emin:
        return 0.0
    k = float(e - emin)/float(emax - emin)
    return k

def computeWeightedCost(gr):
    el = gr.getEdges()
    cost = 0.0
    for e in el:
        cost += e.weight
    return cost
