import sys
import os

import topgen.parameters
import topgen.generator
import topgen.optimal

def parse_config_file(config_file):
    if config_file == None:
        print 'Error: Missing config file!'
        return None
    ip = open(config_file)
    configs = ip.read().split('\n')
    conf = {}
    for c in configs:
        s = c.split('=')
        if len(s) < 2:
            continue
        conf[s[0]] = s[1]
    files = []
    if 'IP_PARAMS_FILE' in conf:
        files.append(conf['IP_PARAMS_FILE'])
    if 'IP_LIST_FILE' in conf:
        files.append(conf['IP_LIST_FILE'])
    if 'OUTPUT_DIR' in conf:
        files.append(conf['OUTPUT_DIR'])
    if 'OPT_MEASURES' in conf:
        files.append(conf['OPT_MEASURES'])
    return files

def topology_generator(config_file):
    if config_file == None:
        print 'Error: Missing config file!'
        return False
    files = parse_config_file(config_file)
    if not topgen.parameters.parameters(files[:2]):
        print 'Error: Problem generating input list'
        return False
    op_dir = files[2] + '/all/'
    if not os.path.exists(op_dir):
        os.makedirs(op_dir)
    #topgen.generator.generate_topologies(files[1], op_dir)
    topgen.optimal.robust_topologies(files[3], op_dir)
    return True


def robust_topologies():
    topgen.optimal.robust_topologies('config/optimality_measures.txt', 'topgen_outputs/all')
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Error: Missing parameters!"
        exit()
    topology_generator(sys.argv[1])
