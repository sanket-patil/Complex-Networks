import math
import sys

if len(sys.argv) < 3:
    print 'Usage: python match-airports-lat-long.py <airline-airport-list> <output-file-name>'
    exit()
ip = open(sys.argv[1])
apts = ip.read().split('\n')
ip.close()
ip = open('code-lat-long.txt')
airports = ip.read().split('\n')
latlong = []
for i in airports:
    if i.split()[0] in apts:
        latlong.append(i)
op = open(sys.argv[2], 'w')
op.write('\n'.join(latlong))
op.close()
ip.close()