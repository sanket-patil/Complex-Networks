% Checks whether a graph is simple (no self-loops, no double edges)
% Gergana Bounova, February 20, 2006

function [isit] = issimple(adj)

% INPUTs: adj - adjacency matrix
% OUTPUTs: isit - a Boolean variable

isit = true;

% check for self-loops
self_loops = find(diag(adj)>0);
if not(isempty(self_loops))
  'graph has self loops'
  isit = false;
  return
end

% check for double edges
double_edges = find(adj>1);
if not(isempty(double_edges))
  'graph has double edges'
  isit = false;
  return
end