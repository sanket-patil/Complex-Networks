import math
import sys

if len(sys.argv) < 3:
    print 'Usage: python', sys.argv[0], '<airline_airport_list> <airline_code_lat_long>'
    exit()
ip = open(sys.argv[1])
apts = ip.read().split('\n')
ip.close()
ip = open(sys.argv[2])
airports = ip.read().split('\n')
ip.close()
for i in airports:
    if i.split()[0] in apts:        
        apts.remove(i.split()[0])
print '.\n'.join(apts)