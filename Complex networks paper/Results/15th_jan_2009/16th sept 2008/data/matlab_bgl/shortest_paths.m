function [d pred] = shortest_paths(A,u,varargin)
% SHORTEST_PATHS Compute the weighted single source shortest path problem.
%
% [d pred] = shortest_paths(A,u) returns the distance (d) and the predecessor
% (pred) for each of the vertices along the shortest path from u to every
% other vertex in the graph.  
% 
% ... = shortest_paths(A,u,options) sets optional parameters (see 
% set_matlab_bgl_options) for the standard options.
%   options.algname: the algorithm to use 
%       [{'auto'} | 'dijkstra' | 'bellman_ford' | 'dag']
%   options.inf: the value to use for unreachable vertices 
%       [double > 0 | {Inf}]
%   options.visitor: a structure with visitor callbacks.  This option only
%       applies to dijkstra or bellman_ford algorithms.  See dijkstra_sp or
%       bellman_ford_sp for details on the visitors.
%   options.edge_weight: a double array over the vertices with an edge
%       weight for each node
%
% Note: 'auto' cannot be used with 'nocheck' = 1.  The 'auto' algorithm
% checks if the graph has negative edges and uses bellman_ford in that
% case, otherwise, it uses 'dijkstra'.  In the future, it may check if the
% graph is a dag and use 'dag'.  
%
% Example:
%    load graphs/clr-25-2.mat
%    shortest_paths(A,1)
%    shortest_paths(A,1,struct('algname','bellman_ford'))
%
% See also DIJKSTRA_SP, BELLMAN_FORD_SP, DAG_SP

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

options = struct('algname', 'auto', 'inf', Inf);
if (length(varargin) > 0)
    options = merge_structs(varargin{1}, options);
end;

if (check)
    % check the values of the matrix
    check_matlab_bgl(A,struct('values',1));
    
    % set the algname
    if (strcmpi(options.algname, 'auto'))
        mv = min(min(A));
        if (mv < 0)
            options.algname = 'bellman_ford';
        else
            options.algname = 'dijkstra';
        end;
    end;
else
    if (strcmpi(options.algname, 'auto'))
        error('shortest_paths:invalidParameter', ...
            'algname auto is not compatible with no check');       
    end;
end;

if (options.inf < 0)
    error('options.inf must be larger than 0');
end;

if (trans)
    A = A';
end;

if (isfield(options,'visitor'))
    [d pred] = matlab_bgl_sp_mex(A,u,lower(options.algname),options.inf,...
        options.visitor);
else
    [d pred] = matlab_bgl_sp_mex(A,u,lower(options.algname),options.inf);
end;

