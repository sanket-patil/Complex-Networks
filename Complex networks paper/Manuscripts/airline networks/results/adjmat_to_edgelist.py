ip1 = open('us/us-airways-airports.txt', 'r')
ip2 = open('us/us-airways-adjacency-matrix.txt', 'r')
ip3 = open('us/us-airways-edge-list.txt', 'w')
airports = ip1.read().split('\n')
adjacency = ip2.read().split('\n')
flights = ''
print len(airports)
print len(adjacency)
for i in range(len(airports)):
    al = adjacency[i].split('\t')
    for j in range(len(al)):
        if int(al[j]) == 1:
            flights += airports[i] + ' ' + airports[j] + '\n'
ip3.write(flights)
ip1.close()
ip2.close()
ip3.close()
