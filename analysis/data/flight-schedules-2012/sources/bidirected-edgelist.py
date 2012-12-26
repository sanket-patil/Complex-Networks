import sys

if len(sys.argv) < 2:
    print 'Usage: python', sys.argv[0], '<airline_edge_list.txt>'
    exit()
ip = open(sys.argv[1])
flights = ip.read().split('\n')
print len(flights)
ip.close()
bidirected = []
for f in flights:
    k = f.split()
    if len(k) < 2:
        continue
    g = k[1] + ' ' + k[0]
    if g in flights:
        if f not in bidirected:
            if g not in bidirected:
                bidirected.append(f)
            else:
                continue
print len(bidirected)
opfile = sys.argv[1].split('.txt')[0] + '-bidirected-edgelist.txt'
op = open(opfile, 'w')
op.write('\n'.join(bidirected))
op.close()
print 'Output file:', opfile