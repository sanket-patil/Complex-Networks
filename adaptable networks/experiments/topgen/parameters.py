import sys

def parse_parameters(params_file):
    if params_file == None:
        print "Error: Missing parameters!"
        return
    ip = open(params_file)
    params = ip.read()
    ip.close()
    params = params.split('\n')
    ip_params = {}
    for p in params:
        if p.find('#') == 0:
            continue
        q = p.split('=')
        if len(q) < 2:
            continue
        ip_params[q[0]] = q[1]
    return ip_params


def generate_inputs(params):
    nmin = 0
    nmax = 0
    nstep = 0   
    if 'n' in params:
        p = params['n'].split()
        if len(p) < 3:
            return None
        nmin = int(p[0])
        nmax = int(p[1])
        nstep = int(p[2])
    directed = False
    if 'directed' in params:
        if params['directed'] == 'True':
            directed = True
    num = 100
    if 'num' in params:
        num = int(params['num'])
    inputs = []
    if not directed:
        for n in range(nmin, nmax, nstep):
            for p in range(2, n, 3):
                for k in range(n - 1, int(n * p/2) + 1, 5):
                    entry = str(num * n) + ' ' + str(int(directed)) + ' ' + str(n) + ' ' + str(p) + ' ' + str(k)
                    inputs.append(entry)
    return inputs


def parameters(files):
    if len(files) < 2:
        print "Error: Missing parameters!"
        return False
    params = parse_parameters(files[0])
    if not params:
        print "Error: Missing parameters!"
        return False
    inputs = generate_inputs(params)
    op = open(files[1], 'w')
    op.write('\n'.join(inputs))
    op.close()
    return True

                          
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Error: Missing parameters!"
        exit()
    print parameters(sys.argv[1:])
