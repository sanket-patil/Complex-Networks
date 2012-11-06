import graph.graph
import graph.node
import graph.edge
import graph.operations
import algorithms.connectivity.connectivity
import algorithms.paths.paths
import algorithms.paths.pathlist
import efficiency.efficiency_measures
import algorithms.importance.betweenness_centrality
import algorithms.paths.bellman_ford
import algorithms.importance.closeness_centrality
import algorithms.importance.degree_centrality
import robustness.robustness_measures
import cost.cost_measures
import fitness.fitness_functions
import algorithms.cycles.girth
import algorithms.neighbourhood.clustering
import random

g = graph.graph.graph(directed = False)
value = []
ip = open('D:\work\Dropbox\Current Workspace\Deterministic Techniques\experiments\bbbnetworks.txt')
edgelists = ip.read().split("\n")
for edgelist in edgelists:
    edgelist = list(edgelist.split(', '))
    print edgelist
    g.create(edgelist, 20)
    eff = efficiency.efficiency_measures.computeEfficiency(g)
    print 'eff', eff
    rob = robustness.robustness_measures.computeRobustness(g)
    #rob = fitness.fitness_functions.connectivityBasedRobustness(g)
    print 'rob', rob
    c = cost.cost_measures.computeCost(g)
    print 'cost', c
    value.append(eff + rob - c)
    g.reset()    
print value
del value[:]
ip.close()
