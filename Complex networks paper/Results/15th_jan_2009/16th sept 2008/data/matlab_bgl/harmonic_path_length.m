% Compute average path length for a network
% Gergana Bounova, December 8, 2005

function [L] = harmonic_path_length(adjL)

% INPUTS: adjL - matrix of weights/distances between nodes
% OUTPUTS: average path length: the average of the shortest paths between
%          every two edges

% Def: the average path length is obtained by find

n = size(adjL,2);
for i=1:n
    for j=i+1:n
        d(i,j) = 1/shortest_path(adjL,adjL,i,j);
    end
end

L = 1/(sum(sum(d))/2/n/(n+1));