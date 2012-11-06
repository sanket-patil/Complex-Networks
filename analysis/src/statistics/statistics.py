
def normalizeTI(tI):
    totalTrust = sum(tI.values())
    if totalTrust == 0:
        return
    for k, v in tI.iteritems():
        tI[k] = float(int((v/totalTrust) * 100000.0))/100000.0    
    return

def computePDF(pdf, vals): 
    for v in vals.values():
        if v in pdf:
            pdf[v] += 1
        else:
            pdf[v] = 1
    return

    
def computeCDF(cdf, pdf):
    keys = pdf.keys()
    for i in range(len(keys)):
        if i == 0:
            cdf[keys[i]] = pdf[keys[i]]
        else:
            cdf[keys[i]] = pdf[keys[i]] + cdf[keys[i - 1]]
    return


def computeParetoCDF(pcdf, pdf):
    keys = pdf.keys()
    n = len(keys)
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            pcdf[keys[i]] = pdf[keys[i]]
        else:
            pcdf[keys[i]] = pdf[keys[i]] + pcdf[keys[i + 1]]
    return
    
def trustVsDistrust(tI, dtI, tdt):
    nodes = tI.keys()
    for nd in nodes:
        tdt[nd] = str(tI[nd]) + '\t' + str(dtI[nd])
    return
    

def computeDistribution(measure):
    dist = {}
    for v in measure.values():
        if dist.has_key(v):
            dist[v] = dist[v] + 1
        else:
            dist[v] = 1
    return dist


def computeParetoDistribution(measure):
    pdf = computeDistribution(measure)
    pcdf = {}
    computeParetoCDF(pcdf, pdf)
    return pcdf