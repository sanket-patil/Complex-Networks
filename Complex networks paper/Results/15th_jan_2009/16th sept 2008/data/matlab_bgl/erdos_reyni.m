function A=erdos_reyni(n,p)
% ERDOS_REYNI Generates a random Erdos-Reyni (Gnp) graph
%
% A=erdos_reyni(n,p) generates a random Gnp graph with n vertices and where
% the probability of each edge is p.  The resulting graph is symmetric.
%
% This function is different from the Boost Graph library version, it was
% reimplemented natively in Matlab.
%
% Example:
%   A = erdos_reyni(100,0.05);

%
% David Gleich
% 21 May 2006
%

%
% 5 April 2007
% Fixed the function so it returns correct output.
%

A = triu(rand(n)<p,1);
A = sparse(A);
A = A+A';

