
def computeDistribution(seq, a = 0.0, b = 1.0, interval = 1, normalization = 1.0):
    dist = {}
    for i in range(int(a/interval), int(b/interval) + 1):
        dist[i] = 0.0
    for i in seq:
        i = int(i/interval)
        dist[i] = dist[i] + 1.0
    for k in dist.keys():
        dist[k] = dist[k]/float(normalization)
    return dist

#def computeContDist(seq, a = 0.0, b = 1.0, interval = 100, normalization = 1.0):
#    dist = {}
#    for i in range(int(a/interval), int(b/interval) + 1):
 #       dist[

def computeCDF(seq, a = 0.0, b = 1.0, interval = 1, normalization = 1.0):
    cdf = {}
    for i in range(int(a/interval), int(b/interval) + 1):
        cdf[i] = 0.0
    dist = computeDistribution(seq, a, b, interval, normalization)
    for i in range(int(a/interval), int(b/interval) + 1):
        if i > int(a/interval):
            cdf[i] = dist[i] + cdf[i - 1]
        else:
            cdf[i] = dist[i]
    return cdf

if __name__ == "__main__":
    print 'Utility module. Computes distribution given a sequence.'
    seq = [100.2, 97, 378.9, 1000, 786, 654, 34.7, 234.6, 542.6, 1098.6, 567.43, 324, 132, 999, 876, 10, 453]
    print computeDistribution(seq, min(seq), max(seq), 100, len(seq))
    print computeCDF(seq, min(seq), max(seq), 100, len(seq))
