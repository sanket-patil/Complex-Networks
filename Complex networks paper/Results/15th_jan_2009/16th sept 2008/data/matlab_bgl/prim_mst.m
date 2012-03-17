function [varargout] = prim_mst(A,options)
% PRIM_MST Compute a minimum spanning with Kruskal's algorithm.
%
% Prim's MST algorithm computes a minimum spanning tree for a graph.
%
% This method works on weighted symmetric graphs without negative edge
% weights.
% The runtime is O(E log (V)).
%
% See MST for calling information.  This function just calls
% mst(...,struct('algname','prim'));
%
% Example:
%    load graphs/clr-24-1.mat
%    prim_mst(A)
%
% See also MST, KRUSKAL_MST.

%
% David Gleich
% 23 April 2006
%

if (nargin > 1)
    options.algname = 'prim';
else
    options = struct('algname','prim');
end;

varargout = cell(1,nargout);

[varargout{:}] = mst(A,options);

