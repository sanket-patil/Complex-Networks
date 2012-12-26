import sys

if len(sys.argv) < 3:
    print 'Usage: python', sys.argv[0], '<airline_bidirected_edgelist> <airline_airport_distances>'
    exit()
ip1 = open(sys.argv[1])
ip2 = open(sys.argv[2])
flights = ip1.read().split('\n')
distances = ip2.read().split('\n')
edgelist = []
for i in distances:
    i = i.split()
    if i[0] + ' ' + i[1] in flights or i[1] + ' ' + i[0] in flights:
        edgelist.append(' '.join(i))
opfile = sys.argv[1].split('.txt')[0] + '-directed-weighted.txt'
op = open(opfile, 'w')
op.write('\n'.join(edgelist))
ip1.close()
ip2.close()
op.close()
