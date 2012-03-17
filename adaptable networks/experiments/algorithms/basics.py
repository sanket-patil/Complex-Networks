''' Computes the basic graph properties: (1) degree sequence (2)
(strong) connectivity etc..'''

import graph

def isGraphConnected(gr):
    gr.nodes[0].colour = "gray"
    bfsqueue = [gr.nodes[0]]
    count = 0
    while bfsqueue:
        nd = bfsqueue.pop(0)
        for n in gr.getNeighbours(nd):
            if n.colour == "white":
                n.colour = "gray"
                bfsqueue.append(n)
        nd.colour = "black"
        count += 1
    gr.resetNodeColours()
    if count == gr.numnodes:        
        return True
    else:
        return False

def computeClusteringCoefficiencts(gr):
    cc = []
    for n in gr.nodes:
        neighbours1 = gr.getNeighbours(n)
        for nd in neighbours:
            neighbours2 = gr.getNeighbours(nd)
            neighbourhood = [n2 for n2 in neighbours2 if n2 in neighbours1]
        print neighbourhood
    return cc

def displayBasicProperties(gr):
    print "\nBasic Analysis:"
    print "No. of nodes: ", gr.numnodes
    print "No. of edges: ", gr.numedges
    print "\nNeighbourhood:"
    for i in gr.nodes:
        print "%s: %s" % (i.name, i.neighbours)
    print "\nEdges (with weights):"
    for i in gr.edges:
        print "%s: %s" % (i.name, i.weight)        
    print "\nConnectivity Information: "
    #num_components = isGraphConnected(gr)
    #if num_components == 1:
    print "Connectivity:", isGraphConnected(gr)
    #else:
       #print "Connectivity: Not connected"
       #print "Number of connected components:", num_components
    print "Degree Information:"
    ds = [i.degree for i in gr.nodes]
    print "Degree Sequence: %s" % ds
    print "Max degree:", max(ds)
    print "Min degree:", min(ds)
    print "Average degree: %f", sum(ds)/gr.numnodes
    print "\nClustering:"
    print "Clustering coeeficients vector: %s" % computeClusteringCoefficiencts(gr)
    
    return   

if __name__ == '__main__':
    print __doc__
    

