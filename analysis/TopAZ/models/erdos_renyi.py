import graph.graph
import algorithms.connectivity.connectivity
import random_graphs

def getErdosRenyiGraph(n, k, directed = False, weighted = False, connected = True):
    if not connected:
        return random_graphs.getRandomGraphs(1, n, k, directed = directed, weighted = weighted)[0]
    gr = graph.graph.graph(directed = directed, weighted = weighted)
    while True:
        el = random_graphs.getRandomGraphs(1, n, k, directed = directed, weighted = weighted)[0]
        gr.create(el, n)
        if not algorithms.connectivity.connectivity.isGraphConnected(gr):
            gr.reset()
            continue
        return el
