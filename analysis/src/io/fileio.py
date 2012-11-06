# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 13:03:53 2012

@author: IC013315
"""

def getEdgeListFromFile(nwFile):
    nwFile = open(nwFile)
    nw = nwFile.read().split('\n')
    nwFile.close()
    numnodes = 0
    while(True):
        if '#' in nw[0]:
            meta = nw.pop(0)
            if 'Nodes:' in meta:
                meta = meta.split()
                numnodes = int(meta[meta.index('Nodes:') + 1])
                if 'Edges:' in meta:
                    numedges = int(meta[meta.index('Edges:') + 1])
        else:
            break
    return (nw, numnodes, numedges)

    
def saveToFile(measure, fileName):
    keys = measure.keys()
    keys.sort()
    op = open(fileName, 'w')
    op.write('\n'.join(['%s\t%s' % (key, measure[key]) for key in sorted(measure.iterkeys())]))
    op.close()
    
    return

    
def save(vals, opFile):
    saveToFile(vals, opFile)
    return