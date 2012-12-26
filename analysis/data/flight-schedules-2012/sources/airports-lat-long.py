import math

ip = open('airports-lat-long.txt')
info = ip.read().split('\n')
ip.close()
latlong = {}
for i in info:
    i = i.split('\t')
    latlong[i[0]] = i[2] + ' ' + i[3]
info = []
for k, v in latlong.items():
    info.append(k + ' ' + v)
op = open('code-lat-long.txt', 'w')
op.write('\n'.join(info))
op.close()
