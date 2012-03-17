import mst
import sys

def findmst(args):
    ip = open(args[0], 'r')
    el = ip.read().split('\n')
    ip.close()
    ip = open(args[1], 'r')
    nodes = ip.read().split('\n')
    ip.close()
    nodeids = {}
    n = len(nodes)
    for i in range(1, n + 1):
        nodeids[nodes[i - 1]] = i
    G = {}
    for u in nodeids.values():
        G[u] = {}
    for u in nodeids.values():
        for v in nodeids.values():
            r = -1.0
            G[u][v] = r
            G[v][u] = r
    cliquecost = 0.0
    for e in el:
        e = e.split()
        i = int(nodeids[e[0]])
        j = int(nodeids[e[1]])
        G[i][j] = float(e[2])
        G[j][i] = float(e[2])
        cliquecost += G[i][j]
    mstree = mst.MinimumSpanningTree(G)
    tree = []
    nodenames = dict([[v, k] for k, v in nodeids.items()])
    for ed in mstree:
        tree.append(nodenames[ed[0]] + ' ' + nodenames[ed[1]])
    mstweight = sum(G[i][j] for i, j in mstree)
    op = open(args[2], 'w')
    op.write('Clique cost: ' + repr(cliquecost) + '\n\n')
    op.write('MST weight: ' + repr(mstweight) + '\n\n')
    op.write('# MST edges: ' + repr(len(tree)) + '\n\n')
    op.write('MST: \n' + '\n'.join(tree))
    return

if __name__ == "__main__":
    findmst(sys.argv[1:])
