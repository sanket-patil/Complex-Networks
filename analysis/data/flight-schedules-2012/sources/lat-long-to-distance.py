import math
import sys

def haversine(pt1, pt2):
    R = 6371.0
    pt1 = pt1.split()
    lat1 = math.radians(float(pt1[0]))
    long1 = math.radians(float(pt1[1]))
    pt2 = pt2.split()
    lat2 = math.radians(float(pt2[0]))
    long2 = math.radians(float(pt2[1]))
    dlat = lat2 - lat1
    dlong = long2 - long1
    a = math.sin(dlat/2.0)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong/2.0)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d

if len(sys.argv) < 2:
    print 'Usage: python', sys.argv[0], '<airline_code_lat_long>'
    exit()
ip = open(sys.argv[1])
info = ip.read().split('\n')
ip.close()
latlong = {}
for i in info:
    i = i.split()
    latlong[i[0]] = i[1] + ' ' + i[2]
dist = []
airports = latlong.keys()
for i in airports:
    for j in airports[airports.index(i) + 1:]:
        d = haversine(latlong[i], latlong[j])
        dist.append(i + ' ' + j + ' ' + str(d))
opfile = sys.argv[1].split('.txt')[0] + '-airports-distances.txt'
op = open(opfile, 'w')
op.write('\n'.join(dist))
op.close()
print 'Output file:', opfile
