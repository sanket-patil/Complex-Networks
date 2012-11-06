import graph.graph
import graph.node
import graph.edge
import graph.operations
import topbreed.random_graphs
import efficiency.efficiency_measures

op = open('digraph-eff-p-k.txt', 'a')
gr = graph.graph.graph(directed = True)
for n in range(20, 50, 2):
    k = 2 * (n - 1)
    op.write('Num nodes: ' + str(n) + '\n')
    op.write('Num edges: ' + str(k) + '\n\n')
    for p in range(1, n):
        op.write('p, epn: ' + str(p) + '\n')
        rgs = topbreed.random_graphs.getRandomGraphs(1000, n, k, p, p, -1, 1, 0)
        aveff = 0.0
        for rg in rgs:
            gr.create(rg, n)
            aveff += efficiency.efficiency_measures.computeEfficiency(gr)
            gr.reset()
        aveff /= len(rgs)
        op.write('Avg Eff: ' + str(aveff) + '\n\n')
op.close()
