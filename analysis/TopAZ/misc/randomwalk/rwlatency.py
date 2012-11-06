import graph.graph
import graph.node
import random

def rwhit(gr, src, dest):
    nd = src
    hit = 0
    while nd != dest:
        nd = gr.getNode(nd)
        neighbours = nd.getNeighbours()
        if len(neighbours) < 1:
            return -1
        nd = random.choice(neighbours)
        hit += 1
    return hit

def rwcommute(gr, src, dest):
    return rwhit(gr, src, dest) + rwhit(gr, dest, src)

def rwaveragehit(gr):
    pass

def rwaveragecommute(gr):
    pass

def rwdia(gr):
    dia = 0
    nl = gr.getNodeList()
    for src in nl:
        for dest in nl:
            if src == dest:
                continue
            hit = rwhit(gr, src, dest)
            if hit > dia:
                dia = hit
    return dia

def rwapl(gr):
    hits = []
    nl = gr.getNodeList()
    for src in nl:
        for dest in nl:
            if src == dest:
                continue
            hits.append(rwhit(gr, src, dest))
    return float(sum(hits))/float(len(hits))

def rwaverageddia(gr):
    dias = []
    for i in range(1000):
        dias.append(rwdia(gr))
    return float(sum(dias))/float(len(dias))

def rwaveragedapl(gr):
    apls = []
    for i in range(1000):
        apls.append(rwapl(gr))
    return float(sum(apls))/float(len(apls))

if __name__ == "__main__":
    print 'Random walk latency'
