import math
import sys

if len(sys.argv) < 3:
    print 'Usage: python', sys.argv[0], '<airline_airport_list> <airport_code_lat_long>'
    exit()
ip = open(sys.argv[1])
apts = ip.read().split('\n')
ip.close()
ip = open(sys.argv[2])
airports = ip.read().split('\n')
ip.close()
latlong = []
for i in airports:
    if i.split()[0] in apts:
        latlong.append(i)
opfile = sys.argv[1].split('.txt')[0] + '-code-lat-long.txt'
op = open(opfile, 'w')
op.write('\n'.join(latlong))
op.close()
print 'Output file:', opfile