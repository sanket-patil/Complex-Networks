import sys

import nwanalysis.nwanalysis as nwa
from io.fileio import getEdgeListFromFile
from io.fileio import save
from statistics import statistics
   
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python main.py <networkInputFile> <resultsOutputDirectory>"
        exit()
    
    el, numnodes, numedges = getEdgeListFromFile(sys.argv[1])
    prefix = sys.argv[2] + '\\' + (sys.argv[1].split('.txt')[0]).split('\\')[-1]
    
    nw = nwa.createNetwork(el)    
    nwa.degreeDistributions(nw, prefix)
    #nwa.betweennessDistributions(nw, prefix)
    #tI_k = {}
    #initialTrust(el, numnodes, tI_k)
    #trustIndices(el, numnodes, tI_k)
    