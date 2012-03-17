% Converts an adjacency graph representation to a list
% (pointers) representation
% Valid for a general (directed, not simple) network model
% Gergana Bounova, March 9, 2006

function [str] = adj2str(adj)

% INPUT: an adjacency matrix, NxN, N - # of nodes

% OUTPUT: data structure with pointers to children

% N = length(adj); % number of nodes

for i=1:length(adj)
  str(i).child = find(adj(i,:)>0);
  str(i).w = adj(i,find(adj(i,:)>0)); % record weights, thus model
                                      % double edges
end

