ip = open('united-edge-list.txt', 'r')
flights = ip.read().split('\n')
print len(flights)
ip.close()
bidirected = []
for f in flights:
    k = f.split()
    g = k[1] + ' ' + k[0]
    if g in flights:
        if f not in bidirected and g not in bidirected:
            bidirected.append(f)
print len(bidirected)
op = open('united-bidirected-edgelist.txt', 'w')
op.write('\n'.join(bidirected))
op.close()
