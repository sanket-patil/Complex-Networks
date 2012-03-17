import math

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

ip = open('us/us-airways-code-lat-long.txt')
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
op = open('us/us-airways-airports-distances.txt', 'w')
op.write('\n'.join(dist))
op.close()
