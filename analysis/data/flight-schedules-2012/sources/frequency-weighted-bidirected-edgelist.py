import sys

if len(sys.argv) < 2:
    print 'Usage: python', sys.argv[0], '<airline_edge_list.txt>'
    exit()
ip = open(sys.argv[1])
flights = ip.read().split('\n')
print len(flights)
ip.close()
freq_bidirected = {}
for f in flights:
    k = f.split()
    if len(k) < 2:
        continue
    g = k[1] + ' ' + k[0]
    if g in flights:
        if not f in freq_bidirected:
            if not g in freq_bidirected:
                freq_bidirected[f] = 1
            else:
                continue
        else:
            freq_bidirected[f] += 1
print len(freq_bidirected)
opfile = sys.argv[1].split('.txt')[0] + '-frequency-bidirected-edgelist.txt'
op = open(opfile, 'w')
edges = ''
for k in freq_bidirected.keys():
    weight = float(1.0/freq_bidirected[k])
    edges = edges + k + ' ' + str(weight) + '\n'
op.write(edges)
op.close()
print 'Output file:', opfile