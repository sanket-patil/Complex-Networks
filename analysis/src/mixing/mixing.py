
def classify(hh, hl, lh, ll, tI, dtI, low):
    nodes = tI.keys()
    for nd in nodes:
        if tI[nd] > low and dtI[nd] > low:
            hh.append(nd)
        elif tI[nd] > low and dtI[nd] <= low:
            hl.append(nd)
        elif tI[nd] <= low and dtI[nd] > low:
            lh.append(nd)
        else:
            ll.append(nd)
    print len(hh), len(hl), len(lh), len(ll)