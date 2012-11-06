import math

def computeEntropy(dist, base = 2):
    H = 0.0
    for k in dist.keys():
        if dist[k] == 0:
            continue
        H += dist[k] * math.log(dist[k], base)
    H *= -1
    return H


if __name__ == "__main__":
    print 'Utility module. Computes entropy given a distribution. Probably some more methods can be added.'
