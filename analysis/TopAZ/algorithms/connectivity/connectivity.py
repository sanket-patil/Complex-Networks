''' Computes the connectivity properties of graphs. '''

import reachability
import scc

def isGraphConnected(gr):
    if not gr.directed:
        if len(reachability.getBFSTree(gr)) == (gr.getNumNodes() - 1):
            return True
        else:
            return False
    else:
        return isGraphStronglyConnected(gr)

def isGraphStronglyConnected(gr):
    if scc.getNumOfSCC(gr) == 1:
        return True
    else:
        return False



if __name__ == '__main__':
    print __doc__
    

