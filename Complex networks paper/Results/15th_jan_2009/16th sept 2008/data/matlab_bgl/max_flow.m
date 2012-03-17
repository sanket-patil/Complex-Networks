function [flowval cut R F] = max_flow(A,u,v,varargin)
% MAX_FLOW Compute the max flow on A from u to v.
%
% flowval=max_flow(A,u,v) computes the maximum flow on the network defined by
% the adjacency structure A, with source u and sink v.
%
% [flowval cut R F] = max_flow(A,u,v) returns the maximum flow in the 
% network A with source u and sink v as well as additional information.  
% For each vertex on the source side of the mincut, mincut(i) = 1, 
% for each vertex on the sink side, mincut(i) = -1.  
% R is the residual graph.  R(i,j) is the amount of unused capacity 
% on edge (i,j).  F is the flow graph, F(i,j) is the amount of used 
% capacity on edge (i,j).  F, A, and R satisfy the relationship A = F + R.
%
% The algorithm used is the push-relabel algorithm.
%
% ... = max_flow(A,optionsu) sets optional parameters (see 
% set_matlab_bgl_options) for the standard options.
%   There are no additional options for this function.
%
% Note: the values on A are interpreted as integers, please round them
% yourself to get the best interpretation.  The code uses the floor of 
% the values in A.
%
% Example:
%    load graphs\max_flow_example.mat
%    max_flow(A,1,8)

%
% David Gleich
% 16 April 2006
%
% 2006-05-31: Added full2sparse check
%

[trans check full2sparse] = get_matlab_bgl_options(varargin{:});
if (full2sparse && ~issparse(A)) 
    A = sparse(A); 
end

if (check)
    % no additional input checks
    check_matlab_bgl(A,struct());
end;


% max_flow will transpose the data inside
if (trans)
end;

if (check)
    % remove any non-zero diagonals
    A = A - diag(diag(A));
end;

n = size(A,1);

if nargout == 2
    [flowval cut] = max_flow_mex(A,u,v);
elseif nargout >= 3
    [flowval cut ri rj rv] = max_flow_mex(A,u,v);
    
    % If anyone needs this operation to be more efficient, send me email, 
    % and I can make max_flow_mex return this more efficiently.
    R = sparse(ri,rj,rv,n,n);
else
    flowval = max_flow_mex(A,u,v);
end;

if (nargout >= 4)
    F = A - R;
end;


