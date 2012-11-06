# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:02:57 2012

@author: IC013315
"""
from io.fileio import saveToFile
from statistics.statistics import computeDistribution
from statistics.statistics import computeParetoDistribution

import networkx as nx

def createNetwork(edges):
    nw = nx.DiGraph()
    nw.graph['name'] = 'epinions-signed-network'
    for edge in edges:
        edge = edge.split('\t')
        if edge[2] == '1':
            w = 1.0
        else:
            w = 0.0
        nw.add_edge(edge[0], edge[1], weight = w)
    return nw

def saveNetwork(nw):
    pass
    return
    
    
def degreeDistributions(nw, prefix):
    totaldegree = nw.degree()
    saveToFile(totaldegree, prefix + '-degrees.txt')
    totaldegreeDist = computeDistribution(totaldegree)
    saveToFile(totaldegreeDist, prefix + '-degree-dist.txt')
    totaldegreeParetoDist = computeParetoDistribution(totaldegree)
    saveToFile(totaldegreeParetoDist, prefix + '-degree-pareto-dist.txt')
    
    totalindegree = nw.in_degree()
    saveToFile(totalindegree, prefix + '-indegrees.txt')
    totalindegreeDist = computeDistribution(totalindegree)
    saveToFile(totalindegreeDist, prefix + '-indegree-dist.txt')
    totalindegreeParetoDist = computeParetoDistribution(totalindegree)
    saveToFile(totalindegreeParetoDist, prefix + '-indegree-pareto-dist.txt')
    
    totaloutdegree = nw.out_degree()
    saveToFile(totaloutdegree, prefix + '-outdegrees.txt')
    totaloutdegreeDist = computeDistribution(totaloutdegree)
    saveToFile(totaloutdegreeDist, prefix + '-outdegree-dist.txt')
    totaloutdegreeParetoDist = computeParetoDistribution(totaloutdegree)
    saveToFile(totaloutdegreeParetoDist, prefix + '-outdegree-pareto-dist.txt')
    
    totalposdegree = nw.degree(weight = 'weight')
    saveToFile(totalposdegree, prefix + '-posdegrees.txt')
    totalposdegreeDist = computeDistribution(totalposdegree)
    saveToFile(totalposdegreeDist, prefix + '-posdegree-dist.txt')
    totalposdegreeParetoDist = computeParetoDistribution(totalposdegree)
    saveToFile(totalposdegreeParetoDist, prefix + '-posdegree-pareto-dist.txt')

    posindegree = nw.in_degree(weight = 'weight')
    saveToFile(posindegree, prefix + '-posindegrees.txt')
    posindegreeDist = computeDistribution(posindegree)
    saveToFile(posindegreeDist, prefix + '-posindegree-dist.txt')
    posindegreeParetoDist = computeParetoDistribution(posindegree)
    saveToFile(posindegreeParetoDist, prefix + '-posindegree-pareto-dist.txt')

    posoutdegree = nw.out_degree(weight = 'weight')
    saveToFile(posoutdegree, prefix + '-posoutdegrees.txt')
    posoutdegreeDist = computeDistribution(posoutdegree)
    saveToFile(posoutdegreeDist, prefix + '-posoutdegree-dist.txt')
    posoutdegreeParetoDist = computeParetoDistribution(posoutdegree)
    saveToFile(posoutdegreeParetoDist, prefix + '-posoutdegree-pareto-dist.txt')
    
#    totalnegdegree = nw.degree(weight = 'weight')
#    saveToFile(totalnegdegree, prefix + '-negdegrees.txt')
#    totalnegdegreeDist = computeDistribution(totalnegdegree)
#    saveToFile(totalnegdegreeDist, prefix + '-negdegree-dist.txt')
#    totalnegdegreeParetoDist = computeParetoDistribution(totalnegdegree)
#    saveToFile(totalnegdegreeParetoDist, prefix + '-negdegree-pareto-dist.txt')
#
#    negindegree = nw.in_degree(weight = 'weight')
#    saveToFile(negindegree, prefix + '-negindegrees.txt')
#    negindegreeDist = computeDistribution(negindegree)
#    saveToFile(negindegreeDist, prefix + '-negindegree-dist.txt')
#    negindegreeParetoDist = computeParetoDistribution(negindegree)
#    saveToFile(negindegreeParetoDist, prefix + '-negindegree-pareto-dist.txt')
#
#    negoutdegree = nw.out_degree(weight = 'weight')
#    saveToFile(negoutdegree, prefix + '-negoutdegrees.txt')
#    negoutdegreeDist = computeDistribution(negoutdegree)
#    saveToFile(negoutdegreeDist, prefix + '-negoutdegree-dist.txt')
#    negoutdegreeParetoDist = computeParetoDistribution(negoutdegree)
#    saveToFile(negoutdegreeParetoDist, prefix + '-negoutdegree-pareto-dist.txt')

    return

def betweennessDistributions(nw, prefix):
    betweenness = nx.betweenness_centrality(G = nw, normalized = True)
    saveToFile(betweenness, prefix + '-betweenness.txt')
    betweennessDist = computeDistribution(betweenness)
    saveToFile(betweennessDist, prefix + '-betweenness-dist.txt')
    betweennessParetoDist = computeParetoDistribution(betweenness)
    saveToFile(betweennessParetoDist, prefix + '-betweenness-pareto-dist.txt')

    posbetweenness = nx.betweenness_centrality(G = nw, normalized = True, weight = 1)
    saveToFile(posbetweenness, prefix + '-posbetweenness.txt')
    posbetweennessDist = computeDistribution(posbetweenness)
    saveToFile(posbetweennessDist, prefix + '-posbetweenness-dist.txt')
    posbetweennessParetoDist = computeParetoDistribution(posbetweenness)
    saveToFile(posbetweennessParetoDist, prefix + '-posbetweenness-pareto-dist.txt')

    negbetweenness = nx.betweenness_centrality(G = nw, normalized = True, weight = -1)
    saveToFile(negbetweenness, prefix + '-negbetweenness.txt')
    negbetweennessDist = computeDistribution(negbetweenness)
    saveToFile(negbetweennessDist, prefix + '-negbetweenness-dist.txt')
    negbetweennessParetoDist = computeParetoDistribution(negbetweenness)
    saveToFile(negbetweennessParetoDist, prefix + '-negbetweenness-pareto-dist.txt')

