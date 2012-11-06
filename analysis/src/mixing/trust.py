# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:33:23 2011

@author: IC013315
"""
from statistics import statistics
from io.fileio import save

def computeStats(tI_k_plus_1, sign, maxiter, prefix):
    statistics.normalizeTI(tI_k_plus_1)
    pdf = {}
    statistics.computePDF(pdf, tI_k_plus_1)    
    cdf = {}
    statistics.computeCDF(cdf, pdf)    
    pcdf = {}
    statistics.computeParetoCDF(pcdf, pdf)
        
    if sign == 1:
        save(tI_k_plus_1,  prefix + '-' + repr(maxiter) + '-trust-index.txt')
        save(pdf, prefix + '-' + repr(maxiter) + '-trust-pdf.txt')
        save(cdf, prefix + '-' + repr(maxiter) + '-trust-cdf.txt')
        save(pcdf, prefix + '-' + repr(maxiter) + '-trust-pcdf.txt')
    elif sign == 0:
        save(tI_k_plus_1,  prefix + '-' + repr(maxiter) + '-distrust-index.txt')
        save(pdf, prefix + '-' + repr(maxiter) + '-distrust-pdf.txt')
        save(cdf, prefix + '-' + repr(maxiter) + '-distrust-cdf.txt')
        save(pcdf, prefix + '-' + repr(maxiter) + '-distrust-pcdf.txt')
    elif sign == 2:
        save(tI_k_plus_1,  prefix + '-' + repr(maxiter) + '-total-trust-index.txt')
        save(pdf, prefix + '-' + repr(maxiter) + '-total-trust-pdf.txt')
        save(cdf, prefix + '-' + repr(maxiter) + '-total-trust-cdf.txt')
        save(pcdf, prefix + '-' + repr(maxiter) + '-total-trust-pcdf.txt')

    pdf.clear()
    cdf.clear()
    return

def initTrust(nw, numnodes, tI_k, sign):
    for i in range(numnodes):
        tI_k[str(i)] = 0.0
    for i in range(len(nw)):
        if len(nw[i]) > 0:
            edge = nw[i].split()
            if sign == 1:
                if int(edge[2]) == 1:
                    tI_k[edge[1]] = tI_k[edge[1]] + int(edge[2])
            elif sign == 0:
                if int(edge[2]) == -1:
                    tI_k[edge[1]] = tI_k[edge[1]] + abs(int(edge[2]))
            elif sign == 2:
                tI_k[edge[1]] = tI_k[edge[1]] + int(edge[2])
            else:
                print 'Invalid sign'
                break
    return
 

def trustIndex(nw, tI_k, maxiter, sign):
    i = 0
    miniter = maxiter/5
    tI_k_plus_1 = None
    o_k = []
    o_k_plus_1 = []
    while(i < maxiter):
        i += 1
        del o_k[:]
        for key in sorted(tI_k.iteritems(), key=lambda (k,v): (v,k)):
            o_k.append(key)
        if sign == 0:
            tI_k_plus_1 = computeDistrustIndex(tI_k, nw)
        elif sign == 1:
            tI_k_plus_1 = computeTrustIndex(tI_k, nw)
        elif sign == 2:
            tI_k_plus_1 = computeTotalTrustIndex(tI_k, nw)
        else:
            print 'Invalid sign'
            break
        del o_k_plus_1[:]
        for key in sorted(tI_k_plus_1.iteritems(), key=lambda (k,v): (v,k)):
            o_k_plus_1.append(key)
        if repr(o_k) == repr(o_k_plus_1):
            print 'iter', i
            if i >= miniter:
                break            
        else:        
            tI_k = tI_k_plus_1
    print 'iter', i
    return tI_k_plus_1


def computeTotalTrustIndex(tI, nw):
    trustIndex = {}
    for i in range(len(nw)):
        edge = nw[i].split()
        if edge[1] in trustIndex:
            if edge[0] in tI:
                trustIndex[edge[1]] = trustIndex[edge[1]] + tI[edge[0]] * int(edge[2])
        else:
            if edge[0] in tI:
                trustIndex[edge[1]] = tI[edge[0]] * int(edge[2])
    for k in tI.keys():
        if k not in trustIndex:
            trustIndex[k] = tI[k]    
    return trustIndex


def computeTrustIndex(tI, nw):
    trustIndex = {}
    for i in range(len(nw)):
        edge = nw[i].split()
        if edge[1] in trustIndex:
            if edge[0] in tI and int(edge[2]) == 1:
                trustIndex[edge[1]] = trustIndex[edge[1]] + tI[edge[0]] * int(edge[2])
        else:
            if edge[0] in tI and int(edge[2]) == 1:
                trustIndex[edge[1]] = tI[edge[0]] * int(edge[2])
    for k in tI.keys():
        if k not in trustIndex:
            trustIndex[k] = tI[k]    
    return trustIndex

def computeDistrustIndex(tI, nw):
    trustIndex = {}
    for i in range(len(nw)):
        edge = nw[i].split()
        if (edge[1] in trustIndex) and (int(edge[2]) == -1):
            if edge[0] in tI:
                trustIndex[edge[1]] = trustIndex[edge[1]] + tI[edge[0]] * abs(int(edge[2]))
        else:
            if (edge[0] in tI) and (int(edge[2]) == -1):
                trustIndex[edge[1]] = tI[edge[0]] * abs(int(edge[2]))
    for k in tI.keys():
        if k not in trustIndex:
            trustIndex[k] = tI[k]    
    return trustIndex