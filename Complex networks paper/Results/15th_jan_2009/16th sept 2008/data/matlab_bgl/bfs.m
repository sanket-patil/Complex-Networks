function [d dt pred] = bfs(A,u,varargin)
% BFS Compute the breadth first search order.
%
% [d dt pred] = bfs(A,u) returns the distance to each vertex (d) and the  
% discover time (dt) in a breadth first search starting from vertex u.
%    d(i) = dt(i) = -1 if vertex i is not reachable from vertex u.
% pred is the predecessor array.  pred(i) = 0 if vertex (i)  
% is in a component not reachable from u and i != u.
%
% This method works on directed graphs.
% The runtime is O(V+E).
%
% ... = bfs(A,u,options) sets optional parameters (see 
% set_matlab_bgl_options) for the standard options.
%   There are no additional options for this function.
%
% Note: this function does not depend upon the non-zero values of A, but
% only uses the non-zero structure of A.
%
% Example:
%    load graphs/bfs_example.mat
%    d = bfs(A,1)
%
% See also DFS

%
% David Gleich
% 19 April 2006
%
% 2006-05-31: Added full2sparse check
%

[trans check full2sparse] = get_matlab_bgl_options(varargin{:});
if (full2sparse && ~issparse(A)) 
    A = sparse(A); 
end
if (check) 
    check_matlab_bgl(A,struct()); 
end
if (trans) 
    A = A'; 
end

[d dt pred] = bfs_mex(A,u);

