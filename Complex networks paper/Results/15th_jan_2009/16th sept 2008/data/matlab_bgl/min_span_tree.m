% Prim's minimal spanning tree algorithm
% Gergana Bounova, March 14, 2005

function [tr] = min_span_tree(adj)

% INPUTS: graph defined by adjacency matrix
% OUTPUTS: matrix specifying minimum spanning tree (subgraph)

% check if graph is connected:
if not(isconnected(adj))
  'graph is not connected, no spanning tree exists'
  return
end

% Prim's alg idea:
%  start at any node, find closest neighbor and mark edge
%  for all remaining nodes, find closest to previous cluster, mark edge
%  continue until no nodes remain

n = length(adj); % number of nodes
tr = zeros(n);

% set all zeros in the matrix to inf
adj(find(adj==0))=inf; 

conn_nodes = 1;
rem_nodes = [2:n];

while length(rem_nodes)>0
  [minlink]=min(min(adj(conn_nodes,rem_nodes)));
  ind=find(adj(conn_nodes,rem_nodes)==minlink);
  ind_j=ceil(ind/length(conn_nodes));
  ind_i=mod(ind,length(conn_nodes));
  if ind_i==0
      ind_i=length(conn_nodes);
  end 
  
  i=conn_nodes(ind_i); j=rem_nodes(ind_j);
  tr(i,j)=1; % tr(j,i)=1;
  conn_nodes = [conn_nodes j];
  rem_nodes = setdiff(rem_nodes,j);
  
end
