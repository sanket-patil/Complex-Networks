function ccfs = clustering_coefficients(A,varargin)
% CLUSTERING_COEFFICIENTS Compute the clustering coefficients for vertices.
%
% ccfs = clustering_coefficients(A) returns the clustering coefficients for
% all vertices in A.  The clustering coefficient is the ratio of the number
% of edges between a vertex's neighbors to the total possible number of 
% edges between the vertex's neighbors. 
%
% This method works on directed or undirected graphs.
% The runtime is O(nd^2) where d is the maximum vertex degree.
%
% ... = clustering_coefficients(A,options) sets optional parameters (see 
% set_matlab_bgl_options) for the standard options.
%   There are no additional options for this function.
%
% Note: this function does not depend upon the non-zero values of A, but
% only uses the non-zero structure of A.
%
% Example:
%    load graphs\clique-10.mat
%    clustering_coefficients(A)

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

ccfs = clustering_coefficients_mex(A);