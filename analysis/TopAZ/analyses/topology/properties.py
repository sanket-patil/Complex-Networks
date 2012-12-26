import graph.graph
import graph.node
import graph.edge
import graph.operations
import algorithms.connectivity.connectivity
import algorithms.connectivity.scc
import algorithms.paths.paths
import algorithms.paths.pathlist
import efficiency.efficiency_measures
import algorithms.importance.betweenness_centrality
import algorithms.paths.bellman_ford
import algorithms.importance.closeness_centrality
import algorithms.importance.degree_centrality
import robustness.robustness_measures
import cost.cost_measures
import cost.cost_measures
import fitness.fitness_functions
import algorithms.cycles.girth
import algorithms.neighbourhood.clustering
import random

def computeProperties(g, opfile = None):
    if not opfile:
        op = open('op.txt', 'a')
    else:
        op = open(opfile, 'w')
    n = g.getNumNodes()
    op.write('numnodes: ' + repr(n) + '\n\n')
    e = g.getNumEdges()
    op.write('numedges: ' + repr(e) +'\n\n')
    op.write('Cost (SECON): ' + repr(cost.cost_measures.computeCost(g)) + '\n\n')
    #op.write('Density (Connectance):' + repr(cost.cost_measures.computeDensity(g)) + '\n\n')
    op.write('edgelist: ' + repr(g.getEdgeList()) + '\n\n')
    op.write('SCC: ' + repr(algorithms.connectivity.scc.getSCC(g)) + '\n\n')
    op.write('EFFICIENCY: ' + '\n\n')
    apsp = algorithms.paths.paths.getAPSP(g)
    nl = g.getNodeList()
    el = g.getEdgeList()
    op.write('diameter: ' + repr(efficiency.efficiency_measures.getDiameter(apsp = apsp)) + '\n\n')
    op.write('apl: ' + repr(efficiency.efficiency_measures.getAPL(apsp = apsp)) + '\n\n')
    ecc = efficiency.efficiency_measures.getNormalizedEcc(apsp = apsp, nl = nl)
    op.write('ecc: ' + repr(sorted(ecc)) + '\n\n')
    op.write('radius: ' + repr(efficiency.efficiency_measures.getRadius(nl = nl, apsp = apsp)) + '\n\n')
    op.write('numradii: ' + repr(efficiency.efficiency_measures.getNumRadii(nl = nl, apsp = apsp)) + '\n\n')
    clv = algorithms.importance.closeness_centrality.getClosenessVectors(nl = nl, apsp = apsp)
    op.write('closeness vectors:' + repr(clv) + '\n\n')
    cldist = sorted(algorithms.importance.closeness_centrality.getCloseDist(nl = nl, apsp = apsp))
    op.write('closeness: ' + repr(cldist) + '\n\n')
    clskew = cldist[-1] - 1.0/float(n)
    op.write('closeness skew: ' + repr(clskew) + '\n\n')
    op.write('ROBUSTNESS: ' + '\n\n')
##    indd = sorted(algorithms.importance.degree_centrality.getInDegSeq(g))
##    totalindd = sum(indd)
##    minindeg, maxindeg, avgindeg = indd[0], indd[-1], float(totalindd)/float(n)
##    op.write('Indegree (min, max, avg): ' + repr(minindeg) + ', ' + repr(maxindeg) + ', ' + repr(avgindeg) + '\n\n')
##    indd = [float(d)/float(totalindd) for d in indd]
##    op.write('Indegree Dist: ' + repr(indd) + '\n\n')
##    inddskew = indd[-1] - 1.0/float(n)
##    op.write('Indegree dist skew: ' + repr(inddskew) + '\n\n')
##    outdd = sorted(algorithms.importance.degree_centrality.getOutDegSeq(g))
##    totaloutdd = sum(outdd)
##    minoutdeg, maxoutdeg, avgoutdeg = outdd[0], outdd[-1], float(totaloutdd)/float(n)
##    op.write('Outdegree (min, max, avg): ' + repr(minoutdeg) + ', ' + repr(maxoutdeg) + ', ' + repr(avgoutdeg) + '\n\n')
##    outdd = [float(d)/float(totaloutdd) for d in outdd]
##    op.write('Outdegree Dist: ' + repr(outdd) + '\n\n')
##    outddskew = outdd[-1] - 1.0/float(n)
##    op.write('Outdegree dist skew: ' + repr(outddskew) + '\n\n')
    ds = algorithms.importance.degree_centrality.getDegreeSequence(g)
    dd = sorted(ds.values())
    totaldd = sum(dd)
    mindeg, maxdeg, avgdeg = dd[0], dd[-1], float(totaldd)/float(n)
    op.write('Degree (min, max, avg): ' + repr(mindeg) + ', ' + repr(maxdeg) + ', ' + repr(avgdeg) + '\n\n')
    op.write('Degree sequence: ' + repr(ds) + '\n\n')
    dd = [float(d)/float(totaldd) for d in dd]
    op.write('Degree Centrality (normalized): ' + repr(dd) + '\n\n')
    ddskew = dd[-1] - 1.0/float(n)
    op.write('Degree centrality skew: ' + repr(ddskew) + '\n\n')
    #nbdist = sorted(algorithms.importance.betweenness_centrality.getNodeBetnDist(nl = nl, apsp = apsp))
##    op.write('Node betweenness: ' + repr(nbdist) + '\n\n')
##    nbs = algorithms.importance.betweenness_centrality.getNodeBetweennessSequence(nl = nl, apsp = apsp)
##    op.write('Node Betweenness Sequence: ' + repr(nbs) + '\n\n')
##    np = float(n * (n - 1))
##    nbdist = sorted([float(v)/np for v in nbs.values()])
##    op.write('Node betweenness (normalized): ' + repr(nbdist) + '\n\n')
##    nbdskew = nbdist[-1] - 1.0/float(n)
##    op.write('node betweenness skew: ' + repr(nbdskew) + '\n\n')
##    ebdist = sorted(algorithms.importance.betweenness_centrality.getEdgeBetnDist(nl = nl, el = el, apsp = apsp))
##    op.write('edge betweenness: ' + repr(ebdist) + '\n\n')
##    ebdskew = ebdist[-1] - 1.0/float(e)
##    op.write('edge betweenness skew: ' + repr(ebdskew) + '\n\n')
    #app = algorithms.paths.paths.getAllPaths(g)
    #connseq = sorted(robustness.robustness_measures.getConnSeq(app = app))
    #connseq = robustness.robustness_measures.getConnectivitySequence(app = app)
    #op.write('conn sequence: ' + repr(connseq) + '\n\n')
    op.write('MISC: ' + '\n\n')
    op.write('Girth: ' + repr(algorithms.cycles.girth.findGirth(g)) + '\n\n')
    clcoeff = sorted([v for v in algorithms.neighbourhood.clustering.getClusteringCoefficient(g).values()])
    cl = sum(clcoeff)/float(g.getNumNodes())
    op.write('clustering coefficients: ' + repr(clcoeff) + '\n\n')
    op.write('clustering coeff: ' + repr(cl) + '\n\n')
    op.write('clustering coeff skew: ' + repr(clcoeff[-1] - cl) + '\n\n')
    op.write('******************' + '\n\n')
    op.close()
    return
