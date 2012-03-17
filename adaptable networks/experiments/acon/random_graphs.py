#import graph.graph
#import algorithms.connectivity.connectivity

import random
import datetime
import math
from operator import itemgetter

def getRandomGraphs(num, n, k, p = -1, epn = -1, alpha = -1, directed = False, weighted = False):
    if p == -1 or p > n - 1:
        p = n - 1
    if epn == -1 or p > n - 1:
        epn = n - 1
    #if p == n - 1 or epn == n - 1:
    #    alpha = 0.0        
    if alpha == -1:
        return createUniformRandomGraphs(num, n, k, p, epn, directed, weighted)
    else:
        return createAlphaBasedRandomGraphs(num, n, k, p, epn, alpha, directed, weighted)


def createUniformRandomGraphs(num, n, k, p = -1, epn = -1, directed = False, weighted = False):
    # Need to implement the weighted part.
    # Probably generate random weights for edges when edges are added
    rgs = []
    degreev = {}
    epnv = {}
    if p == -1 or p > n - 1:
        p = n - 1
    if epn == -1 or p > n - 1:
        epn = n - 1
    maxed = n * p/2
    if directed:
        maxed = n * epn
    #rand = random.SystemRandom()
    for i in range(num):
        rg = []
        for key in range(1, n + 1):
            degreev[str(key)] = 0
            epnv[str(key)] = 0
        count = 0        
        candidates = degreev.keys()
        while count < k and count < maxed:
            if len(candidates) < 2:
                break
            n1 = random.choice(candidates)
            if epnv[n1] >= epn:
                continue
            n2 = random.choice(candidates)
            if degreev[n2] >= p:
                continue
            if n2 == n1:
                continue
            ed = n1 + " " + n2
            if ed in rg:
                if len(candidates) == 2 or len(candidates) % 2:
                    break
                continue
            if not directed:
                de = n2 + " " + n1
                if de in rg:
                    if len(candidates) == 2 or len(candidates) % 2:
                        break
                    continue
            rg.append(ed)            
            epnv[n1] = epnv[n1] + 1
            if not directed:
                degreev[n1] = degreev[n1] + 1
            degreev[n2] = degreev[n2] + 1
            count += 1
            if not directed:
                if degreev[n1] == p or epnv[n1] == epn:
                    candidates.remove(n1)
                if degreev[n2] == p or epnv[n2] == epn:
                    candidates.remove(n2)
            else:
                if degreev[n1] == p and epnv[n1] == epn:
                    candidates.remove(n1)
                if degreev[n2] == p and epnv[n2] == epn:
                    candidates.remove(n2)
        rgs.append(rg)        
    return rgs


def createAlphaBasedRandomGraphs(num, n, k, p, epn, alpha, directed, weighted):
    rgs = []
    degreev = {}
    epnv = {}
    if p == -1 or p > n - 1:
        p = n - 1
    if epn == -1 or p > n - 1:
        epn = n - 1
    maxed = n * p/2
    if directed:
        maxed = n * epn
    rand = random.SystemRandom()    
    connected = False
    while len(rgs) < num:
        rg = []
        for key in range(1, n + 1):
            degreev[str(key)] = 0
            epnv[str(key)] = 0
        count = 0        
        candidates = degreev.keys()
        while count < k and count < maxed:
            if len(candidates) < 2:
                break
            if directed:
                if random.random() < 0.95:
                #if count >= 1 and count <= k/2:
                    n1 = choseNode(candidates, epnv, alpha)
                else:
                    n1 = random.choice(candidates)
                if epnv[n1] >= epn:
                    continue
            else:
                n1 = random.choice(candidates)
                if epnv[n1] >= epn or degreev[n1] >= p:
                    #cadidates.remove(n1)
                    continue
            if directed:
                if random.random() < 0.95:
                #if count >= k/2: #and random.random() < 0.95:
                    n2 = choseNode(candidates, degreev, alpha)
                else:
                    n2 = random.choice(candidates)
                if degreev[n2] >= p:
                    #candidates.remove(n2)
                    continue
            else:
                if count >= 1:
                    n2 = choseNode(candidates, degreev, alpha)
                else:
                    n2 = random.choice(candidates)
                if degreev[n2] >= p or epnv[n2] >= epn:                    
                    continue
            if n2 == n1:
                continue
            ed = n1 + " " + n2
            if ed in rg:
                if len(candidates) == 2 or len(candidates) % 2:
                    break
                continue
            if not directed:
                de = n2 + " " + n1
                if de in rg:
                    if len(candidates) == 2 or len(candidates) % 2:
                        break
                    continue
            rg.append(ed)
            epnv[n1] = epnv[n1] + 1
            if not directed:
                degreev[n1] = degreev[n1] + 1
            degreev[n2] = degreev[n2] + 1
            count += 1
            if not directed:
                if degreev[n1] >= p or epnv[n1] >= epn:
                    candidates.remove(n1)
                if degreev[n2] >= p or epnv[n2] >= epn:
                    candidates.remove(n2)
            else:
                if degreev[n1] >= p and epnv[n1] >= epn:
                    candidates.remove(n1)
                if degreev[n2] >= p and epnv[n2] >= epn:
                    candidates.remove(n2)
        rgs.append(rg)
##        if not directed:
##            gr = graph.graph.graph(directed = directed, weighted = weighted)
##            gr.create(rg, n)
##            if algorithms.connectivity.connectivity.isGraphConnected(gr):
##                connected = True
##            if len(rgs) == num and connected == False:            
##                rgs.pop()
    return rgs

def createWattsStrogatzRandomGraphs():
    pass

def choseNode(candidates, degree, alpha):
    shortlist = []
    shortlist.extend(sorted(degree.iteritems(), key = itemgetter(1), reverse = True))
    sl = []
    for entry in shortlist:
        if entry[0] not in candidates:
            sl.append(entry)
    for i in sl:
        shortlist.remove(i)
    del sl[:]
    begin = int(len(shortlist) * alpha)
    if alpha < 0.25:
        windowsz = int(math.floor(len(shortlist) * 0.01))
    else:
        windowsz = int(math.ceil(len(shortlist) * 0.1))
    if begin >= len(shortlist):
        begin -= windowsz
    window = shortlist[begin: begin + windowsz + 1]
    nd = random.choice(window)[0]
    del shortlist[:]
    return nd


if __name__ == '__main__':
    rgs = getRandomGraphs(100000, 10, 9, 9, 9, -1, 0, 0)
    print len(rgs)
    #print rgs

