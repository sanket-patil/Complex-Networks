
def findGirth(gr):
    return girth(gr)

def girth(gr):
    girth = gr.getNumNodes() + 1
    nl = gr.getNodeList()
    s = []
    r = []
    parent = {}
    depth = {}
    for v in nl:
        r.append(v)
        parent[v] = ''
        depth[v] = 0
        while r:
            x = r.pop()
            s.append(x)
            for y in gr.getNode(x).getNeighbours():
                if y == parent[x]:
                    continue
                if not y in s:
                    parent[y] = x
                    depth[y] = depth[x] + 1
                    r.append(y)
                else:
                    girth = min(girth, depth[x] + depth[y] + 1)
        del r[:]
        parent.clear()
        depth.clear()
        del s[:]
    return girth

def DFS(gr, nd = None):
    if not nd:
        nd = gr.getNodes()[0]
    dfsstack = []
    depth = {}
    d = 0
    girth = gr.getNumNodes() + 1
    search(nd, dfsstack, depth, d)
    while dfsstack:
        ed = dfsstack.pop()
        print 'ed:', ed
        ed = ed.split()
        v = ed[0]
        w = gr.getNode(ed[1])
        if not w.visited:
            print 'depth (if):', repr(depth)
            search(w, dfsstack, depth, depth[v] + 1)
        else:
            print 'depth (else):', repr(depth)
            if depth[v] - depth[w.name] == 1:
                continue
            g = depth[v] - depth[w.name] + 1
            if g < 2:
                continue
            if g < girth:
                print v, w.name
                girth = g
    gr.resetNodeVisitedFlags()
    del dfsstack[:]
    depth.clear()
    return girth

def search(v, l, depth, d):
    v.visited = True
    depth[v.name] = d
    for w in v.getNeighbours():
        l.append(v.name + " " + w)
    return
