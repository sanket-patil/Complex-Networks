import graph.graph
import random
import fitness.fitness_functions

def produceOffsprings(params, matingpool):
    CLONE = 0.1
    EQED = 0.20
    TWOPT = 0.40
    CNS = 0.50    
    EQND = 0.60
    CPED = 0.70
    TXED = 0.75
    BFED = 0.85
    BFND = 1.0
    d = False
    w = False
    params = params.split()    
    if params[0] == '1':
        d = True
    n = int(params[1])
    if len(params) > 7:
        if params[7] == 'w':
            w = True
    offsprings = []
    children = []
    gr1 = graph.graph.graph(directed = d, weighted = w)
    gr2 = graph.graph.graph(directed = d, weighted = w)
    for m1 in matingpool:
        for m2 in matingpool:
            cotype = random.random()
            if cotype <= CLONE:
                offsprings.append(m1)
                continue
            elif cotype <= EQED:                
                equalEdgesCO(m1, m2, children)
            elif cotype <= TWOPT:
                twoPointCO(m1, m2, children)
            elif cotype <= CNS:
                cutAndSpliceCO(m1, m2, children)
            elif cotype <= EQND:
                equalNodesCO(m1, m2, children, gr1, gr2, params)
            elif cotype <= CPED:
                copyEdgesCO(m1, m2, children, gr1, gr2, params)
            elif cotype <= BFED:
                bestFitEdgesCO(m1, m2, children, gr1, gr2, params)
            else:
                bestFitNodesCO(m1, m2, children, gr1, gr2, params)
            if children:
                offsprings.extend(children)
                del children[:]
                gr1.reset()
                gr2.reset()
    validateOffsprings(params, offsprings)
    return offsprings

def equalEdgesCO(m1, m2, children):
    if m1 and m2:
        children.append(m1[:len(m1)/2] + m2[len(m2)/2:])
        children.append(m2[:len(m2)/2] + m1[len(m1)/2:])
    return

def twoPointCO(m1, m2, children):
    if m1 and m2:
        children.append(m1[:len(m1)/4] + m2[len(m2)/4: 3 * len(m2)/4] + m1[3 * len(m1)/4:])
        children.append(m2[:len(m2)/4] + m1[len(m1)/4: 3 * len(m1)/4] + m2[3 * len(m2)/4:])
    return

def cutAndSpliceCO(m1, m2, children):
    if m1 and m2:
        children.append(m1[:len(m1)/2] + m2[len(m2)/2:])
        children.append(m2[:len(m2)/2] + m1[len(m1)/3:])
    return

def equalNodesCO(m1, m2, children, gr1, gr2, params):
    if m1 and m2:
        gr1.create(m1, params[1])
        gr2.create(m2, params[1])
        nodes1 = gr1.getNodes()
        nodes2 = gr2.getNodes()
        m14 = []
        for nd in nodes1[:len(nodes1)/2]:
            m14.extend(nd.getEdgeList())
        for nd in nodes2[len(nodes2)/2:]:
            m14.extend(nd.getEdgeList())
        children.append(m14)
        m32 = []
        for nd in nodes2[:len(nodes1)/2]:
            m32.extend(nd.getEdgeList())
        for nd in nodes1[len(nodes1)/2:]:
            m32.extend(nd.getEdgeList())
        children.append(m32)
    return

def copyEdgesCO(m1, m2, children, gr1, gr2, params):
    if m1 and m2:
        gr1.create(m1, params[1])
        gr2.create(m2, params[1])
        nodes1 = gr1.getNodes()
        nodes2 = gr1.getNodes()
        count = random.choice(range(len(nodes1)))
        src1 = []
        for i in range(count):
            src1.append(random.choice(nodes1))
        count = random.choice(range(len(nodes2)))
        src2 = []
        for i in range(count):
            src2.append(random.choice(nodes2))
        offspring1 = []
        offspring1.extend(m1)
        offspring2 = []
        offspring2.extend(m2)
        offspring3 = []
        offspring3.extend(m1)
        offspring4 = []
        offspring4.extend(m2)
        if len(src1) > 0:
        #nd1 = random.choice(nodes1)
            nd2 = random.choice(nodes2)
            for nd1 in src1:
                #if len(dest2) <= 0:
                #    break
                #nd2 = random.choice(dest2)
                for n in nd1.getNeighbours():
                    if random.random() < 0.5:
                        ed = nd2.getName() + ' ' + n                    
                    else:
                        ed = n + ' ' + nd2.getName()
                    offspring1.insert(0, ed)
                    offspring4.insert(0, ed)
                    m1.insert(0, ed)
            #m1.append(ed)                    
        if len(src2) > 0:
            nd2 = random.choice(nodes1)
            for nd1 in src2:
                #if len(dest1) <= 0:
                #    break
                #nd2 = random.choice(dest1)
                for n in nd1.getNeighbours():
                    if random.random < 0.5:
                        ed = nd2.getName() + ' ' + n
                    else:
                        ed = n + ' ' + nd2.getName()
                    offspring2.insert(0, ed)
                    offspring3.insert(0, ed)
        children.append(offspring1)
        children.append(offspring2)
        children.append(offspring3)
        children.append(offspring4)
        #nd1 = random.choice(nodes1)
        #nd2 = random.choice(nodes2)
        children.append(m1)
        #children.append(m2)
        del src1[:]
        del src2[:]
        return

def transferEdgesCO(m1, m2, children, gr1, gr2, params):
    if m1 and m2:
        gr1.create(m1, params[1])
        gr2.create(m2, params[1])
        nodes1 = gr1.getNodes()
        nodes2 = gr1.getNodes()
        offspring1 = []
        offspring1.extend(m1)
        offspring2 = []
        offspring2.extend(m2)
        ed1 = random.choice(offspring1)
        nd1 = random.choice(nodes1)
        nd2 = random.choice(nodes2)
        if random.random() < 0.5:
            ed2 = nd1.getName() + ' ' + ed1[1]                   
        else:
            ed2 = ed1[0] + ' ' + nd1.getName()
        offspring1.insert(0, ed2)
        if random.random() < 0.5:
            ed2 = nd2.getName() + ' ' + ed1[1]                   
        else:
            ed2 = ed1[0] + ' ' + nd2.getName()
        offspring2.insert(0, ed2)
        offspring1.remove(ed1)
        children.append(offspring1)
        children.append(offspring2)        
        return
    
def bestFitEdgesCO(m1, m2, children, gr1, gr2, params):
    if m1 and m2:
        gr1.create(m1, params[1])
        gr2.create(m2, params[1])
        f1 = fitness.fitness_functions.computeFitness(gr1, alpha = float(params[5]), beta = float(params[6]))
        f2 = fitness.fitness_functions.computeFitness(gr2, alpha = float(params[5]), beta = float(params[6]))
        edges1 = gr1.getEdgeList()
        edges2 = gr2.getEdgeList()
        child1 = []
        child2 = []
        if f1 > f2:
            child1.extend(edges1[:3 * len(edges1)/4])
            child1.extend(edges2[3 * len(edges2)/4:])
            child2.extend(edges1)
        else:
            child1.extend(edges2[:3 * len(edges2)/4])
            child1.extend(edges1[3 * len(edges1)/4:])
            child2.extend(edges2)
        children.append(child1)
        children.append(child2)
    return

def bestFitNodesCO(m1, m2, children, gr1, gr2, params):
    if m1 and m2:
        gr1.create(m1, params[1])
        gr2.create(m2, params[1])
        f1 = fitness.fitness_functions.computeFitness(gr1, alpha = float(params[5]), beta = float(params[6]))
        f2 = fitness.fitness_functions.computeFitness(gr2, alpha = float(params[5]), beta = float(params[6]))
        nodes1 = gr1.getNodes()
        nodes2 = gr2.getNodes()
        child1 = []
        child2 = []
        if f1 > f2:
            for nd in nodes1[:3 * len(nodes1)/4]:
                child1.extend(nd.getEdgeList())                
            for nd in nodes2[3 * len(nodes2)/4:]:
                child1.extend(nd.getEdgeList())
            for nd in nodes1:
                child2.extend(nd.getEdgeList())
        else:
            for nd in nodes2[:3 * len(nodes2)/4]:
                child1.extend(nd.getEdgeList())
            for nd in nodes1[3 * len(nodes1)/4:]:
                child1.extend(nd.getEdgeList())
            for nd in nodes2:
                child2.extend(nd.getEdgeList())
        children.append(child1)
        children.append(child2)
    return

def validateOffsprings(params, offsprings):
    degreev = {}
    epnv = {}
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
    maxed = n * p/2
    if directed:
        maxed = n * epn
    k = int(params[4])
    valided = []
    for os in offsprings:        
        # The node names are hardcoded. Assumed to be numbers between 1 and n
        for key in range(1, n + 1):
            degreev[str(key)] = 0
            epnv[str(key)] = 0
        edcount = 0
        for ed in os:
            e = ed.split()
            n1 = e[0]
            n2 = e[1]            
            if n1 == n2:
                continue
            if not directed:      
                if degreev[n1] == p or epnv[n1] == epn:
                    continue
                if degreev[n2] == p or epnv[n2] == epn:
                    continue
            else:
                if epnv[n1] == epn:
                    continue
                if degreev[n2] == p:
                    continue
            if ed in valided:
                continue
            if not directed:
                de = n2 + ' ' + n1
                if de in valided:
                    continue
            valided.append(ed)
            epnv[n1] = epnv[n1] + 1
            if not directed:
                degreev[n1] = degreev[n1] + 1
            degreev[n2] = degreev[n2] + 1
            edcount += 1
            if edcount == k or edcount == maxed:
                break
        del os[:]
        k = min(k, maxed)
##        for i in range(k):
##            if len(valided) <= 0:
##                break
##            ed = random.choice(valided)
##            os.append(ed)
##            valided.remove(ed)        
        for ed in valided:
            os.append(ed)
        del valided[:]
    return


if __name__ == "__main__":
    param = ""
    matingpool = [['1 2', '3 4', '5 6'], ['7 8', '9 10', '11 12'], ['13 14', '15 16', '17 18', '19 20']]
    offsprings = []
    produceOffsprings(param, matingpool, offsprings)
    print offsprings
