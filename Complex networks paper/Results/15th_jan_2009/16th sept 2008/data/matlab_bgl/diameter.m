% Maximum minimum distance between nodes in the network
% Gergana Bounova, Last Updated: March 9, 2006

function [d] = diameter(adj)

% input: adjacency matrix
% output: network diameter

n = length(adj);

dij = [];

if isdirected(adj)

  for i=1:n
    for j=1:n
      [dij(length(dij)+1)]= shortest_path(adj,adj,i,j);
    end
  end

  d = max(dij);
  return
  
else % undirected graph - cut comp time by 2
  for i=1:n
    for j=i+1:n
      [dij(length(dij)+1)]= shortest_path(adj,adj,i,j);
    end
  end
  
  d = max(dij);
  return
  
end
  
