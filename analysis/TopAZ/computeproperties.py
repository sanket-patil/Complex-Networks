import analyses.topology.properties
import graph.graph
import os
import sys

if len(sys.argv) < 3:
	print "Usage: python main.py <networkInputFile> <resultsOutputDirectory>"
	exit()
airline = open(sys.argv[1])
dirpath = sys.argv[2]
el = airline.read().split('\n')
gr = graph.graph.graph(directed = False, weighted = False)
gr.create(el)
analyses.topology.properties.computeProperties(gr, os.path.join(dirpath, sys.argv[1] + '-properties.txt'))
gr.reset()
airline.close()