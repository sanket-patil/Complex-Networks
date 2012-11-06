import math

ip = open('us/us-airways-airports.txt')
usairports = ip.read().split('\n')
ip.close()
ip = open('code-lat-long.txt')
airports = ip.read().split('\n')
latlong = []
for i in airports:
    if i.split()[0] in usairports:
        latlong.append(i)
op = open('us/us-airways-code-lat-long.txt', 'w')
op.write('\n'.join(latlong))
op.close()
ip.close()
