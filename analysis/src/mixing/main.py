# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:42:27 2011

@author: IC013315
"""

    

   


   
if __name__ == "__main__":    
    
    
    low = 0.0005
    hh = []
    hl = []
    lh = []
    ll = []
    mixing.classify(hh, hl, lh, ll, tI_k_plus_1, dtI_k_plus_1, low)
    tI_k.clear()
    tI_k_plus_1.clear()
    del hh[:]
    del hl[:]
    del lh[:]
    del ll[:]
