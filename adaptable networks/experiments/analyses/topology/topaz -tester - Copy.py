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

gr = graph.graph.graph(directed = False)
edgelist = ['1 16', '12 16', '14 4', '1 2', '1 18', '9 14', '13 16', '12 14', '19 8', '11 7', '19 10', '2 15', '5 6', '17 19', '11 10', '20 13', '6 18', '7 20', '3 10', '7 9', '6 9', '4 11', '20 2', '15 8', '3 4', '15 3', '5 12', '13 8', '5 17', '17 18']
gr.create(edgelist, 20)
print 'dia', efficiency.efficiency_measures.getDiameter(gr)
print 'rob', robustness.robustness_measures.computeRobustness(gr)
print 'ed', gr.getNumEdges()
#value = []
#ip = open('ip.txt')
#edgelists = ip.read().split("\n")
##for edgelist in edgelists:
##    edgelist = list(edgelist.split(', '))
##    print edgelist
##    g.create(edgelist, 20)
##    eff = efficiency.efficiency_measures.computeEfficiency(g)
##    print 'eff', eff
##    rob = robustness.robustness_measures.computeRobustness(g)
##    #rob = fitness.fitness_functions.connectivityBasedRobustness(g)
##    print 'rob', rob
##    c = cost.cost_measures.computeCost(g)
##    print 'cost', c
##    value.append(eff + rob - c)
##    g.reset()
##print value
#ip.close()
