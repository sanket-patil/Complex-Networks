import sys
import os

import graph.graph
import robustness.robustness_measures
import algorithms.connectivity
import algorithms.paths.paths

def get_params(filename):
    f = filename.split('-')
    params = {}
    params['directed'] = f[1]
    params['n'] = f[2]
    params['p'] = f[3]
    params['k'] = f[4]
    return params

def create_buckets(top_dir):
    buckets = []
    for r in [0.5, 0.6, 0.7, 0.8, 0.9]:
        bucket = str(r) + '--' + str(r + 0.1)
        buckets.append(bucket)
    for bucket in buckets:
        open(top_dir + '/' + bucket, 'a').close()
    return buckets


def get_directory(params, top_dir, rob_measure):
    top_dir = top_dir.split('/')[:-3]
    top_dir.append(rob_measure)
    if params['directed'] == '0':
        top_dir.append('undirected')
    else:
        top_dir.append('directed')
    top_dir.append(params['n'])
    top_dir.append(params['p'])
    top_dir.append(params['k'])
    top_dir = '/'.join(top_dir)
    if not os.path.exists(top_dir):
        os.makedirs(top_dir)
    return top_dir


def robust_topologies(measures, topologies_dir):
    if not measures or not topologies_dir:
        return False
##    m = open(measures)
##    measures = m.read().split('\n')
##    m.close()
##    rob_measure = ''
##    for m in measures:
##        m = m.split('=')
##        if m[0] == 'robustness':
##            rob_measure = m[1]
    topologies_files = os.listdir(topologies_dir)
    gr = graph.graph.graph()
    for f in topologies_files:
        params = get_params(f)
        top_dir = topologies_dir.split('/')[:-3]
        top_dir = '/'.join(top_dir)
        op = top_dir + '/' + params['n'] + '-' + params['p'] + '-' + params['k']
        results = []
        #top_dir = get_directory(params, topologies_dir, rob_measure)
        #buckets = create_buckets(top_dir)
        n = int(params['n'])
        f = topologies_dir + '/' + f
        f = open(f)
        topologies = f.read()
        topologies = topologies.split('\n*****\n')
        topologies = topologies[:-1]
        for t in topologies:
            t = t.split('\n')
            gr.create(t, n)            
            #add_to_bucket(gr.getEdgeList(), rob, top_dir, buckets)
            result = compute_properties(gr)
            if not result:
                gr.reset()
                continue
            results.append(result)            
            gr.reset()
        op = open(op, 'w')
        op.write('\n*****\n'.join(results))
    return True


def compute_properties(gr):
    if not algorithms.connectivity.connectivity.isGraphConnected(gr):
        return None    
    result = 'graph: ' + repr(gr.getEdgeList()) + '\n\n'
    apspmatrix = algorithms.paths.paths.getAPSPMatrix(gr)    
    apspmatrix = '\n'.join(apspmatrix)
    result += 'shortest paths:\n' + apspmatrix + '\n\n'  
    rob = robustness.robustness_measures.computeDRI(gr)
    result += 'robustness (degree based): ' + str(rob) + '\n'
    rob = robustness.robustness_measures.computeNBRI(gr)    
    result += 'robustness (node betweenness based): ' + str(rob) + '\n'
    rob = robustness.robustness_measures.nbBasedFNRI(gr)    
    result += 'robustness (percentage nodes in the largest connected component upon deletion of the most central node): ' + str(rob) + '\n'
    return result


def add_to_bucket(el, rob, top_dir, buckets):
    if rob > 0.9:
        op = open(top_dir + '/' + buckets[-1], 'a')
        op.write('\n'.join(el))
        op.write('\n' + 'robustness=' + str(rob))
        op.write('\n*****\n')
    elif rob > 0.8:
        op = open(top_dir + '/' + buckets[-2], 'a')
        op.write('\n'.join(el))
        op.write('\n' + 'robustness=' + str(rob))
        op.write('\n*****\n')
    elif rob > 0.7:
        op = open(top_dir + '/' + buckets[-3], 'a')
        op.write('\n'.join(el))
        op.write('\n' + 'robustness=' + str(rob))
        op.write('\n*****\n')
    elif rob > 0.6:
        op = open(top_dir + '/' + buckets[-4], 'a')
        op.write('\n'.join(el))
        op.write('\n' + 'robustness=' + str(rob))
        op.write('\n*****\n')
    elif rob > 0.5:
        op = open(top_dir + '/' + buckets[-5], 'a')
        op.write('\n'.join(el))
        op.write('\n' + 'robustness=' + str(rob))
        op.write('\n*****\n')
    return


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Error: Missing parameters!"
        exit()
    print robust_topologies(sys.argv[1:])
