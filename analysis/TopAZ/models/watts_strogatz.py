#import graph.graph
#import algorithms.connectivity.connectivity

import random
import datetime
import math
from operator import itemgetter

def getWattsStrogatzGraphs(num, n, p, k = 0, beta = 0.0, directed = False, weighted = False):
    wsrgs = []
    for i in range(num):
        wsrg = []
        createRingLattice(n, p, directed, wsrg)
        if beta > 0.0:
            rewire(wsrg, n, beta, directed)
        wsrgs.append(wsrg)
    return wsrgs

def createRingLattice(n, p, directed, wsrg):
    for i in range(1, n + 1):        
        for j in range(1, int(p/2) + 1):
            j = i + j
            if j > n:
                j %= n
            ed = str(i) + ' ' + str(j)
            wsrg.append(ed)
    return

def rewire(wsrg, n, beta, directed):
    for ed in wsrg:
        i = int(ed.split()[0])
        if random.random() <= beta:
            while True:
                j = random.choice(range(1, n + 1))
                if j == i:
                    continue
                newed = str(i) + ' ' + str(j)
                if newed in wsrg:
                    continue
                if not directed:
                    newde = str(j) + ' ' + str(i)
                    if newde in wsrg:
                        continue
                pos = wsrg.index(ed)
                wsrg.remove(ed)
                wsrg.insert(pos, newed)
                break
    return

if __name__ == '__main__':
    rgs = getWattsStrogatzGraphs(1, 64, 6, beta = 0.0, directed = False)
    for rg in rgs:
        print len(rg)
        print rg
