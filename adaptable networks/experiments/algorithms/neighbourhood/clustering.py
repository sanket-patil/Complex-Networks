
def getClusteringCoefficient(gr, nd = None):
    if gr:
        clcoeffs = {}        
        nodes = gr.getNodes()
        for nd in nodes:
            clcoeffs[nd.name] = 0.0
        for nd in nodes:
            neighbours = nd.getNeighbourhood()
            cluster = 0
            nn = len(neighbours)
            if nn <= 1:
                clcoeffs[nd.name] = 0.0
                continue
            for i in range(nn):
                for j in range(i + 1, nn):
                    if gr.getNode(neighbours[j]).isInNeighbourhood(neighbours[i]):
                        cluster += 1
            clcoeffs[nd.name] = 2 * float(cluster)/float(nn * (nn - 1))
        return clcoeffs
                
