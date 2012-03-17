''' Single Source Shortest Paths: BFS based Algorithm '''
import sys
import pathlist
import path

def bfsBasedShortestPaths(gr, nd, allsp = False):
   paths = {}
   bfsqueue = []
   for v in gr.getNodes():
       paths[v.name] = pathlist.pathlist()
   bfsqueue.append(nd)
   paths[nd].addPath(path.path([nd]))
   while bfsqueue:
      u = bfsqueue.pop(0)
      u = gr.getNode(u)
      u.visited = True
      for v in u.getNeighbours():
         v = gr.getNode(v)
         if not v.visited:
            if not allsp:
               v.visited = True
            plen = sys.maxint
            if paths[v.name].getPathList():
               plen = paths[v.name].getPath().getPathLength()
            for p in paths[u.name].getPathList():
               if p.getPathLength() >= plen:
                  break
               q = []
               for n in p.getPathString().split():
                  q.append(n)
               q.append(v.name)
               paths[v.name].addPath(path.path(q))
            if v.name not in bfsqueue:
               bfsqueue.append(v.name)
   paths[nd].reset()
   del paths[nd]
   gr.resetNodeVisitedFlags()
   return paths
       
def getShortestPathsFrom(gr, nd):
    pass

def getShortestPathBetween(gr, nd1, nd2):
    pass

def getShortestPathsBetween(gr, nd1, nd2):
    pass

if __name__ == "__main__":
    print __doc__
    
