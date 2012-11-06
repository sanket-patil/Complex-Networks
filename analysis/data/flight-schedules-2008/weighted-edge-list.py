ip1 = open('us-airways-airports-distances.txt', 'r')
ip2 = open('us-airways-bidirected-edgelist.txt', 'r')
ip3 = open('us-airways-bidirected-weighted-edge-list.txt', 'w')
distances = ip1.read().split('\n')
flights = ip2.read().split('\n')
edgelist = []
for i in distances:
    i = i.split()
    if i[0] + ' ' + i[1] in flights or i[1] + ' ' + i[0] in flights:
        edgelist.append(' '.join(i))
ip3.write('\n'.join(edgelist))
ip1.close()
ip2.close()
ip3.close()
