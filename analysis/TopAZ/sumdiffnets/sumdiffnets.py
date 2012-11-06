import math

def balancedBaseBNotation(n, b):
    if b % 2:
        low = -1 * int(b/2)
        high = int(b/2)
    else:
        low = -1 * (b/2 - 1)
        high = b/2
    print low, high
    balanced = []
    while abs(n) > 0:        
        n, r = divmod(n, b)
        print n, r
        if r <= high:
            balanced.append(r)
        else:
            balanced.append(r - b)
            n += 1
        print balanced
        print n
    balanced.reverse()
    return balanced
    
def baseBNotation(n, b):
    baseb = []
    while n >= b:
        baseb.append(n % b)
        n = int(n/b)
    baseb.append(n)
    baseb.reverse()
    return baseb


def bbnetwork(b, k):
    fingers = []
    for i in range(0, k):
        fingers.append(pow(b, i))
    el = []
    for i in range(0, pow(b, k)):
        for f in fingers:               
           el.append(str(i) + ' ' + str((i + f) % pow(b, k)))
    return el

def bbbnetwork(b, k):
    fingers = []
    for i in range(0, k):
        fingers.append(pow(b, i))
    el = []
    high = (pow(b, k) - 1)/2
    low = -1 * (pow(b, k) - 1)/2
    n = pow(b, k)
    for i in range(high, low - 1, -1):
        for f in fingers:
            j = i + f
            if j > high:
                j = j - n
            el.append(str(i) + ' ' + str(j))
    return el


if __name__ == "__main__":
    for i in range(3, 6):
        for j in range(1, 6):
            ip = open('bbbn' + '-' + str(i) + '-' + str(j) + '.txt', 'w')
            ip.write('\n'.join(bbbnetwork(i, j)))
            ip.close()
