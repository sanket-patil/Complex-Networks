import initialization
import selection
#import mutation
import crossover

import random

def breed(inputfile, outputdir):    
    ip = open(inputfile)
    breedParams = ip.read()
    ip.close()
    breedParams = breedParams.split("\n")
    # This is hardcoded. Put it in a config file later.
    INITIALSETSZ = 1000
    MATINGPOOLSZ = 50
    matingpool = []
    offsprings = []
    #MUTATIONRATE = 0.005
    #mutationpool = []
    for param in breedParams:
        if not param:
            break
        op = outputdir + '-'.join(param.split()) + '.txt'
        op = open(op, 'a')
        seedgraphs = initialization.getSeedGraphs(INITIALSETSZ, param)
##        for i in range(int(len(seedgraphs) * MUTATIONRATE)):
##            mutationpool.append(random.choice(seedgraphs))
##        mutation.mutate(param, mutationpool)
##        del mutationpool[:]
        selection.selectGraphs(MATINGPOOLSZ, seedgraphs, matingpool, param, op)
        maxiter = 20
        for iter in range(maxiter):
            crossover.produceOffsprings(param, matingpool, offsprings)
            del matingpool[:]
##            for i in range(int(len(offsprings) * MUTATIONRATE)):
##                mutationpool.append(random.choice(offsprings))
##            mutation.mutate(param, mutationpool)
##            del mutationpool[:]
            selection.selectGraphs(MATINGPOOLSZ, offsprings, matingpool, param, op)
            del offsprings[:]
##            avlen = 0
##            for m in matingpool:
##                avlen += len(m)
##            avlen /= len(matingpool)
##        op.write('\n\n')
##        op.write('*****************')
        op.close()
    return


if __name__ == "__main__":
    breed('in.txt')
    
    # post mutation, check termination conditions such as number of iterations, and tolerance
    # this time I should do a lot more number of rounds somehow (may be by selecting smaller populations.)
    # may be post mutation, check about the saturation condition -- if fitnesses are saturating,
    # one can stop after a few more iterations. Or may be it is a local optima. Should I then increase mutation rate? A dynamic mutation rate?
