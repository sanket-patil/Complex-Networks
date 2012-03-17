''' Functions to return the number of Strongly Connected Components.
Algorithms implemented: (1) Kosaraju's algorithm'''

import reachability

def kosarajuSCC(gr):
    nodes = gr.getNodeList()
    stack = []
    sccomponents = []
    while len(stack) != len(nodes):
        for nd in nodes:
            if nd not in stack:
                reachability.DFS(gr, stack, nd)
                stack.append(nd)
    gr.reverse()
    gr.resetNodeVisitedFlags()
    while stack:
        scc = []
        v = stack.pop()
        reachability.DFS(gr, scc, v) 
        scc.append(v)
        sccomponents.append(scc)
        stack = [v for v in stack if v not in scc]
    gr.reverse()
    del stack[:]
    gr.resetNodeVisitedFlags()
    return sccomponents

def getNumOfSCC(gr):
    return len(kosarajuSCC(gr))

def getLargestSCC(gr):
    sccs = getSCC(gr)
    return max([(len(scc), scc) for scc in sccs])[1]

def sizeOfLargestSCC(gr):
    return len(getLargestSCC(gr))

def getSCC(gr):
    return kosarajuSCC(gr)

if __name__ == '__main__':
    print __doc__
    

