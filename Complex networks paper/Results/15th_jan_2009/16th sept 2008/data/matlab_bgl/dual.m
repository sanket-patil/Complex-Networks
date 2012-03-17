% Finds the dual of a graph 
% A dual is the inverted nodes-edges graph
% Gergana Bounova, February 13, 2006

function [adjd] = dual(adj)

% INPUTs: adj - adjacency matrix of the original graph
% OUTPUTs: adjd - adjacency matrix of the dual graph

inc = adj2inc(adj);
adjd = inc2adj(inc');

