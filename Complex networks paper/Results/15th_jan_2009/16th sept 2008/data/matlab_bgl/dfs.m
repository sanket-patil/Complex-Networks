function [d dt ft pred] = dfs(A,u,varargin)
% DFS Compute the depth first search times.
%
% [d dt ft pred] = dfs(A,u) returns the distance (d), the discover (dt) and
% finish time (ft) for each vertex in the graph in a depth first search 
% starting from vertex u.
%   d = dt(i) = ft(i) = -1 if vertex i is not reachable from u
% pred is the predecessor array.  pred(i) = 0 if vertex (i)  
% is in a component not reachable from u and i != u.
% 
% ... = dfs(A,u,options) sets optional parameters (see 
% set_matlab_bgl_options) for the standard options.
%   options.full: compute the full dfs instead of the dfs of
%      the current component (see Note 1) [{0} | 1]
%
% Note 1: When computing the full dfs, the vertex u is ignored, vertex 1 is
% always used as the starting vertex.  
%
% Note: this function does not depend upon the non-zero values of A, but
% only uses the non-zero structure of A.
%
% Example:
%    load graphs/dfs_example.mat
%    d = dfs(A,1)
%
% See also BFS

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

% parse the optional parameters
full = 0;
if (length(varargin) > 0)
    optionsu = varargin{1};
    if (isfield(optionsu,'full'))
        full = optionsu.full;
    end;
end;

[d dt ft pred] = dfs_mex(A,u,full);

