import sys

def insertpolygons(p):
    nws = []
    udnw = []
    dnw = []
    n = p[0]    
    for i in range(1, n + 1):
        j = i + 1
        if j > n:
            j %= n
        udnw.append(str(i) + ' ' + str(j))
        dnw.append(str(i) + ' ' + str(j))
    p.pop(0)
    polygons = len(p)
    outerseglen = int(n/p[0])
    for i in range(polygons):        
        root = 1 + i * int(outerseglen/polygons)
        seglen = int(n/p[i])        
        for j in range(p[i]):
            s = root + j * seglen
            if s > n:
                s %= n
            t = s + seglen
            if t > n:
                t %= n
            udnw.append(str(s) + ' ' + str(t))
            if i % 2:
                dnw.append(str(t) + ' ' + str(s))
            else:
                dnw.append(str(s) + ' ' + str(t))
    nws.append(udnw)
    nws.append(dnw)
    return nws
    
if __name__ == "__main__":
    ip = open(sys.argv[1], 'r')
    parameters = ip.read().split('\n')
    ip.close()
    for p in parameters:
        q = [int(a) for a in p.split()]
        nws = insertpolygons(q)
        op = open('-'.join(p.split()) + '-ud.txt', 'w')
        op.write('\n'.join(nws[0]))
        op.close()
        op = open('-'.join(p.split()) + '-d.txt', 'w')
        op.write('\n'.join(nws[1]))
        op.close()
