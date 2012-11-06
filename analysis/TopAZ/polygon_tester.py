import sys

import graph.graph
import polygon_embedding.directed
import algorithms.paths.paths

def polygon_tester(argv):    
    edgelist = polygon_embedding.directed.directed(int(argv[0]), int(argv[1]), int(argv[2]))
    g = graph.graph.graph(directed = True)
    g.create(edgelist)
    apsp = algorithms.paths.paths.getAPSP(g)
    k = apsp.keys()[0]
    diapath = apsp[k].getPath()
    diameter = diapath.getPathLength()
    for v in apsp.values():
        lp = v.getLongestPath()
        if not lp:
            return -1
        lpl = lp.getPathLength()
        if lpl > diameter:
            diameter = lpl
            diapath = lp
    return 'parameters: ' + repr(argv) + '\n' + 'dia: ' + str(diameter) + '\t' + 'diapath: ' + repr(diapath.getPathString()) + '\n' + 'graph: ' + ', '.join(edgelist)

def prepare_input(N):
    params = []
    for i in range(N, 4, -20):
        print i
        for j in range(4, int(i/2) + 1, 4):
            params.append(str(i) + ' ' + str(j) + ' ' + str(1))
            params.append(str(i) + ' ' + str(j) + ' ' + str(-1))
    return params

if __name__ == "__main__":
    params = prepare_input(int(sys.argv[1]))
    print params
    results = []
    for p in params:
        results.append(polygon_tester(p.split()))
    op = open(sys.argv[2], 'w')
    op.write('\n\n'.join(results))
    op.close()
