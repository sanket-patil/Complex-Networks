% Converts a list representation to an adjacency matrix
% representation
% Valid for a general graph: directed, not simple
% Gergana Bounova, March 9, 2006

function [adj] = str2adj(str)

% INPUT: list with pointers to children

% OUTPUT: an adjacency matrix, NxN, N - # of nodes

n = length(str); % number of nodes
adj = zeros(n); % initialize adjacency matrix

for i=1:n
  adj(i,str(i).child) = str(i).w;
end

