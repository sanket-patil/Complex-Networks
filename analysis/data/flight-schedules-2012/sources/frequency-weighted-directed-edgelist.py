import sys

if len(sys.argv) < 2:
    print 'Usage: python', sys.argv[0], '<airline_edge_list.txt>'
    exit()
ip = open(sys.argv[1])
flights = ip.read().split('\n')
print len(flights)
ip.close()
freq_directed = {}
for f in flights:
    k = f.split()
    if len(k) < 2:
        continue
    if not f in freq_directed:
        freq_directed[f] = 1
    else:
        freq_directed[f] += 1
print len(freq_directed)
opfile = sys.argv[1].split('.txt')[0] + '-frequency-directed-edgelist.txt'
op = open(opfile, 'w')
edges = ''
for k in freq_directed.keys():
    weight = float(1.0/freq_directed[k])
    edges = edges + k + ' ' + str(weight) + '\n'
op.write(edges)
op.close()
print 'Output file:', opfile