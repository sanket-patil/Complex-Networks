function [A xy] = cycle_graph(n)
% CYCLE_GRAPH Generate the cycle graph of order n
%
% The cycle graph is a simple cycle with n vertices.
%
% [A xy] = cycle_graph(n) generates a cycle graph with n vertices and
% returns the adjacency matrix in A.  The matrix xy stores two-dimensional 
% coordinates for each vertex.
%
% Example:
%   [A xy] = cycle_graph(10);
%   gplot(A,xy);
%
% See also WHEEL_GRAPH, STAR_GRAPH

i = 1:n;
j = [i(2:end) i(1)];
A = sparse(i,j,1,n,n);
A = A|A';

xy = [cos(2*pi*(i./n))' sin(2*pi*(i./n))'];