% Compute average path length for a network
% Valid for a general graph, (un)directed
% Gergana Bounova, December 8, 2005

function [L,Lall] = ave_path_length(adj)

% INPUTS: adjL - matrix of weights/distances between nodes
% OUTPUTS: average path length: the average of the shortest paths between
%          every two edges

% Def: the average path length is obtained by find

n = size(adj,2);

if isdirected(adj)
  
  for i=1:n
    for j=1:n
      d(i,j) = shortest_path(adj,adj,i,j);
    end
  end

  L = sum(sum(d))/(n*n);
  Lall = d(1:size(d,1)*size(d,2)); % record all paths
  return
  
else % undirected graph, cut comp time by 2
  
  for i=1:n
    for j=i+1:n
      d(i,j) = shortest_path(adj,adj,i,j);
    end
  end

  L = sum(sum(d))/(n*(n-1)/2);
  Lall = d(1:size(d,1)*size(d,2)); % record all paths
  
  return
  
end