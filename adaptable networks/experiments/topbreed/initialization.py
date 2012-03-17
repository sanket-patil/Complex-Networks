import random_graphs

def getSeedGraphs(num, params):
    # Need to remove the hardcoded '7'. Could have more or less params.
    # Also, better validation needs to be done for the params.
    params = params.split()
    if len(params) < 7:
        return None
    directed = False
    if params[0] == '1':
        directed = True
    n = int(params[1])
    p = int(params[2])
    epn = int(params[3])
    k = int(params[4])
    alpha = float(params[5])
    weighted = False
    if params[6] == 'w':
        weighted = True
    seedgraphs = None
    seedgraphs = random_graphs.getRandomGraphs(num, n, k, p, epn, -1, directed, weighted)
    #seedgraphs = random_graphs.getRandomGraphs(num, n, k)
    #if not directed:
    #seedgraphs = random_graphs.getRandomGraphs(int(num * 0.99), n, k, p, epn, -1, directed, weighted)
    #specialseeds = random_graphs.getRandomGraphs(int(num * 0.01), n, k, p, epn, alpha, directed, weighted)
    #seedgraphs.extend(specialseeds)
    #print 'initialized'
    #seedgraphs = random_graphs.getRandomGraphs(num, n, k, p, epn, alpha, directed, weighted)
    #else:
    #    seedgraphs = random_graphs.getRandomGraphs(num, n, k, p, epn, -1, directed, weighted)    
    return seedgraphs


def createSeedGraphs(params):
    pass


if __name__ == "__main__":
    print getSeedGraphs(100, '0 16 15 15 15 0.0 uw')
    #print getSeedGraphs(100, '0 128 7 7 1000 -1 uw')
