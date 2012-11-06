import sys

def powergraph(n, p):
    el = []
    for i in range(1, n):
        el.append(str(i) + ' ' + str(i + 1))
    el.append(str(n) + ' ' + str(1))
    for root in range(1, p + 1):
        i, j = root, root + p
        while j <= n:
            el.append(str(i) + ' ' + str(j))
            i, j = j, j + p
        el.append(str(i) + ' ' + str(j % n))
    return el

if __name__ =="__main__":
    ip = open(sys.argv[1])
    cases = ip.read().split('\n')
    ip.close()
    for case in cases:
        case = case.split()
        el = powergraph(int(case[0]), int(case[1]))
        op = open('-'.join(case) + '.txt', 'w')
        op.write('\n'.join(el))
        
