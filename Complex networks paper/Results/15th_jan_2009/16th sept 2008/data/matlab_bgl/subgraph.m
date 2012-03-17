% This function outputs the adjacency matrix of a subgraph given the
% supergraph and the node subset order of the subgraph
% Gergana Bounova, January 5, 2006

function [adj_sub] = subgraph(adj,A)

% INPUTs: adj - supergraph adjacency matrix
%         A - order (vector) of subgraph nodes

% OUTPUTs: adj_sub - adjacency matrix of the subgraph

adj_sub = adj(A,A);

