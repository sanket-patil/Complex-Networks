import sys

if len(sys.argv) < 2:
    print 'Usage: python', sys.argv[0], '<airline_edge_list.txt>'
    exit()
ip = open(sys.argv[1])
flights = ip.read().split('\n')
print len(flights)
ip.close()
undirected = []
for f in flights:
    k = f.split()
    if len(k) < 2:
        continue
    g = k[1] + ' ' + k[0]
    if f not in undirected:
        if g not in undirected:
            undirected.append(f)
        else:
            continue
print len(undirected)
opfile = sys.argv[1].split('.txt')[0] + '-undirected-edgelist.txt'
op = open(opfile, 'w')
op.write('\n'.join(undirected))
op.close()
print 'Output file:', opfile