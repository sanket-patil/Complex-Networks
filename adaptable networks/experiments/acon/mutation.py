import random
import math

def mutate(n, mutationpool):
    #n = int(params.split()[1])
    REPLACE = 0.6
    REVERSE = 0.7
    ADD = 0.75
    REMOVE = 1.0
    for offspring in mutationpool:
        if len(offspring) <= 0:
            continue
        #print 'before', offspring
        numop = random.choice(range(1, int(math.log(n, 2))))
        for i in range(numop):
            operation = random.random()
            if operation <= REPLACE:
                replaceEdge(params, offspring)
            elif operation <= REVERSE:
                reverseEdge(params, offspring)
            elif operation <= ADD:
                addEdge(params, offspring)
            else:
                removeEdge(offspring)
        #print 'after', offspring
    return

def addEdge(params, offspring, ed = None):
    candidates = getCandidates(params, offspring)
    if not candidates:
        return False
    if len(candidates) < 2:
        return False
    if ed:
        if ed[0] in candidates and ed[1] in candidates:
            offspring.append(ed[1] + ' ' + ed[0])
            return True
        return False
    directed = False
    if params.split()[0] == '1':
        directed = True
    while True:        
        n1 = random.choice(candidates)        
        n2 = random.choice(candidates)
        if n2 == n1:
            continue
        ed = n1 + ' ' + n2
        if ed in offspring:
            if len(candidates) == 2 or len(candidates) % 2:
                return False
            continue
        if not directed:
            de = n2 + ' ' + n1
            if de in offspring:
                if len(candidates) == 2 or len(candidates) % 2:
                    return False
                continue
        offspring.append(ed)
        break
    return True

def removeEdge(offspring):
    ed = random.choice(offspring)
    offspring.remove(ed)
    return ed

def reverseEdge(params, offspring):
    ed = random.choice(offspring)
    if not addEdge(params, offspring, ed.split()):
        offspring.append(ed)
    return

def replaceEdge(params, offspring):
    ed = removeEdge(offspring)
    if not addEdge(params, offspring):
        offspring.append(ed)
    return

def getCandidates(params, offspring):    
    params = params.split()
    directed = False
    if params[0] == '1':
        directed = True
    n = int(params[1])
    p = int(params[2])
    if p == -1 or p > n - 1:
        p = n - 1
    epn = int(params[3])
    if epn == -1 or epn > n - 1:
        epn = n - 1
    k = int(params[4])
    if len(offspring) == k:
        return None
    candidates = []
    degreev = {}
    epnv = {}
    for i in range(1, n + 1):
        i = str(i)
        degreev[i] = 0
        epnv[i] = 0
        candidates.append(i)
    for ed in offspring:
        e = ed.split()
        n1 = e[0]
        n2 = e[1]
        epnv[n1] = epnv[n1] + 1
        if not directed:            
            degreev[n1] = degreev[n1] + 1
        degreev[n2] = degreev[n2] + 1
        if not directed:
            if degreev[n1] == p or epnv[n1] == epn:
                if n1 in candidates:
                    candidates.remove(n1)
            if degreev[n2] == p or epnv[n2] == epn:
                if n2 in candidates:
                    candidates.remove(n2)
        else:
            if degreev[n1] == p and epnv[n1] == epn:
                if n1 in candidates:
                    candidates.remove(n1)
            if degreev[n2] == p and epnv[n2] == epn:
                if n2 in candidates:
                    candidates.remove(n2)
    return candidates
