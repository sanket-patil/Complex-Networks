import os, subprocess, random
import sys

import efficiency
import robustness
import graph.graph
import efficiency.efficiency_measures
import robustness.robustness_measures
import cost.cost_measures

def getFittestTopology(f):
    ip = open(f, "r")
    contents = ip.read()
    if len(contents) == 0:
        return None
##    if contents.find('***Average') != -1:
##        print f
##        ip.close()
    contents = '\n'.join(contents.replace('\r', '').split('\n\n')).split('\n')
    ip.close()
    fitness = []
    top = []
    #print contents    
    while len(contents) > 3:
        contents.pop(0) 
        fitness.append(float(contents[0].split(': ')[1]))
        contents.pop(0)
        top.append(contents[0].split(': ')[1])
        contents.pop(0)
        if(contents[0].find('fittst') != -1):
            contents.pop(0)
        contents.pop(0)        
    return top[fitness.index(max(fitness))]


def getValues(ipfile, target):
    values = []
    ipfile = open(ipfile, 'r')
    edgelists = ipfile.read().split('\n')
    gr = graph.graph.graph(directed = False)
    for el in edgelists[:]:
    #count = 0
    #while len(edgelists) > 0 and count < 1000:
        #el = random.choice(edgelists)
        if len(el) < 2:
            continue
        #count += 1
        #edgelists.remove(el)        
        d, n, el = el.split('#')
        el = el.split(',')
        gr.create(el, int(n))
        eta = efficiency.efficiency_measures.computeEfficiency(gr)
        #eta = efficiency.efficiency_measures.aplBasedEff(gr)
        rho = robustness.robustness_measures.computeDRI(gr)
        #rho = robustness.robustness_measures.RNFNRI(gr)
        #rho = robustness.robustness_measures.nbBasedFNRI(gr)
        kappa = cost.cost_measures.computeCost(gr)
        if eta < 0 or rho < 0 or kappa < 0:
            print n
            print eta, rho, kappa
            continue
        params = str(kappa) + ' ' + str(eta) + ' ' + str(rho)
        values.append(params)
        gr.reset()    
    f = open(target, 'w')
    f.write('\n'.join(sorted(values)))
    f.close()
    return 0
    
def getTopologies(argv):
    if len(argv) < 2:
        print "Insufficient parameters"
        return -1
    source = argv[0]
    target = argv[1]
    directories = [os.path.join(source, f) for f in os.listdir(source) if os.path.isdir(os.path.join(source, f))]
    dirs = []
    for d in directories:
        dirs.extend([os.path.join(d, f) for f in os.listdir(d) if os.path.isdir(os.path.join(d, f))])    
    files = []
    #files = [os.path.join(source, f) for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]    
    for d in dirs:
        files.extend([os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))])
    topologies = []
    for f in files[:]:
        temp = f.split('/')[-1].split()
        direction, n = temp[0], temp[1]
        top = getFittestTopology(f)
        if top == None:
            continue
        topologies.append(direction + '#' + n + '#' + top)        
    f = open(target, 'w')
    f.write('\n'.join(topologies))
    f.close()    
    return 0

if __name__=="__main__":
    #getTopologies(sys.argv[1:])
    getValues(sys.argv[1], sys.argv[2])
