# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 20:30:52 2011

@author: IC013315
"""
import sys

trustFile = open(sys.argv[1])
trust = trustFile.read().split('\n')
trustFile.close()
tI = {}
for i in range(len(trust)):
    t = trust[i].split()
    tI[t[0]] = float(t[1])
distrustFile = open(sys.argv[2])
distrust = distrustFile.read().split('\n')
distrustFile.close()
dtI = {}
for i in range(len(distrust)):
    dt = distrust[i].split()
    dtI[dt[0]] = float(dt[1])

nodes = tI.keys()
tdt = []
for nd in nodes:
    tdt.append(repr(tI[nd]) + '\t' + repr(dtI[nd]))
tdtFile = open(sys.argv[3], 'w')
tdtFile.write('\n'.join(tdt))
tdtFile.close()

low = 0.0005
hh = hl = lh = ll = 0
for nd in nodes:
    if tI[nd] > low and dtI[nd] > low:
        hh += 1
    elif tI[nd] > low and dtI[nd] <= low:
        hl += 1
    elif tI[nd] <= low and dtI[nd] > low:
        lh += 1
    else:
        ll += 1
print hh, hl, lh, ll