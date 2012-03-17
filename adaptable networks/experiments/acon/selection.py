import random
import bisect
import graph.graph
import fitness

def selectGraphs(num, population, matingpool, params, op):   
    #rouletteBasedSelection(int(num * 0.8), population, matingpool, params, op)
    #randomSelection(int(num * 0.2), population, matingpool)
    rouletteBasedSelection(num, population, matingpool, params, op)
    return

def rouletteBasedSelection(num, population, matingpool, params, op):
    params = params.split()
##    d = False
##    if params[0] == '1':
##        d = True
##    n = params[1]
##    w = False
##    if params[6] == 'w':
##        w = True
    n = int(params[0])
    cumulativefs = []
    fs = []
    #gr = graph.graph.graph(directed = d, weighted = w)
    gr = graph.graph.graph()
    el = population[0]
    gr.create(el, n)
    f = fitness.computeFitness(gr)
    cumulativefs.append(f)
    fs.append(f)    
    gr.reset()
    ms = 0    
    for el in population[1:]:
        gr.create(el, n)
        f = fitness.computeFitness(gr)
        cumulativefs.append(cumulativefs[-1] + f)
        fs.append(f)
        gr.reset()
    av = cumulativefs[-1] / len(cumulativefs)
    op.write("Average Fitness: " + str(av) + '\n')
    op.write("Max fitness: " + str(max(fs)) + '\n')
    op.write('fittest: ' + str(population[fs.index(max(fs))]) + '\n')
    op.write("Min fitness: " + str(min(fs)) + '\n\n')
    for i in range(num):
        rnd = random.uniform(0, cumulativefs[-1])
        index = bisect.bisect_left(cumulativefs, rnd)
        matingpool.append(population[index])
    del fs[:]
    del cumulativefs[:]
    return

def randomSelection(num, population, matingpool):
    for i in range(num):
        matingpool.append(random.choice(population))
    return

def mateAlreadySeen(mate, mates, directed):
    print 'len:', len(mates)    
    for m in mates:
        if len(m) != len(mate):
            continue
        count = 0
        for ed in mate:
            if ed in m:
                count += 1                
##            elif not directed:
##                de = ed.split()
##                de.reverse()
##                de = ' '.join(de)
##                if de in m:
##                    count += 1
            else:
                break
        if count == len(mate):
            return mates.index(m)
    return -1
        
    
if __name__ == "__main__":
    pass
