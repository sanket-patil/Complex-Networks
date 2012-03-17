import sys
import parameters
import models.random_graphs

def generate_topologies(ip_file, op_dir):
    if not ip_file:
        return False
    ip = open(ip_file)
    ip_list = ip.read().split('\n')
    for ip in ip_list:
        ip = ip.split()
        if len(ip) < 4:
            continue
        num, directed, n, p, k = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]), int(ip[4])
        topologies = models.random_graphs.getRandomGraphs(n = n, p = p, k = k, num = num)
        st = ''
        numtop = 0
        for t in topologies:
            if len(t) < k:
                continue
            st += '\n'.join(t)
            st += '\n*****\n'
            numtop += 1        
        op_file = open(op_dir + str(numtop) + '-' + str(directed) + '-' + str(n) + '-' + str(p) + '-' + str(k), 'w')
        op_file.write(st)
        op_file.close()
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Error: Missing parameters!"
        exit()
    topgen(sys.argv[1])
