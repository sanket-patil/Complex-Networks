import sys

if len(sys.argv) < 2:
    print 'Usage: python', sys.argv[0], '<airline_edge_list.txt>'
    exit()
ip = open(sys.argv[1])
flights = ip.read().split('\n')
print len(flights)
ip.close()
directed = []
for f in flights:
    k = f.split()
    if len(k) < 2:
        continue    
    if f not in directed:
        directed.append(f)
print len(directed)
opfile = sys.argv[1].split('.txt')[0] + '-directed-edgelist.txt'
op = open(opfile, 'w')
op.write('\n'.join(directed))
op.close()
print 'Output file:', opfile