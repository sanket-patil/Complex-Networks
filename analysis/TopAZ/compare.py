import polygoninsertion.powergraphs
import polygoninsertion.polygoninsertion
import graph.graph
import efficiency.efficiency_measures
import math

gr = graph.graph.graph()
op1 = open('n-r-graphs.dat', 'a')
#op1.write('n\tp\tdpower\tdpoly\n')
#op2 = open('compare-poly-power-graphs-1.txt', 'w')
for n in range(100, 1000):
    for p in range(2, int(n/2)+1):
        #if n % p != 0:
         #   continue
        el = polygoninsertion.powergraphs.powergraph(n, p)
        gr.create(el)
##        op2.write(str(n) + '\t' + str(p) +'\n\n')
##        op2.write('All polygons: ')
##        op2.write(repr(el))
##        op2.write('\n\n')
        dpower = efficiency.efficiency_measures.getDiameter(gr)
        if dpower < math.ceil(math.floor(n/2)/p):
            print((n, p, dpower))
        del el
        gr.reset()
##        el = polygoninsertion.polygoninsertion.insertpolygons([n, int(n/p)])[0]
##        op2.write('Single polygon: ')
##        op2.write(repr(el))
##        op2.write('\n\n')
##        gr.reset()
##        gr.create(el)            
##        dpoly = efficiency.efficiency_measures.getDiameter(gr)
##        del el
##        gr.reset()
        #op1.write(str(n) + '\t' + str(p) + '\t' + str(dpower) + '\t' + str(dpoly) + '\n')
        op1.write(str(n) + ' ' + str(p) + ' ' + str(dpower) + '\n')
op1.close()
#op2.close()
