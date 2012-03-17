function [out1 out2 out3] = mst(A,varargin)
% MST Compute a minimum spanning tree for an undirected graph A.
%
% There are two ways to call MST.
% T = mst(A)
% [i j v] = mst(A) 
% The first call returns the minimum spanning tree T of A.  
% The second call returns the set of edges in the minimum spanning tree.  
% The calls are related by 
%    T = sparse(i,j,v,size(A,1), size(A,1)); 
%    T = T + T';
% The optional algname parameter chooses which algorithm to use to compute
% the minimum spanning tree.  Note that the set of edges returned is not
% symmetric and the final graph must be explicitly symmetrized.
%
% This method works on undirected graphs.
%
% ... = mst(A,optionsu) sets optional parameters (see 
% set_matlab_bgl_options) for the standard options.
%   options.algname: the minimum spanning tree algorithm
%     ['prim' | {'kruskal'}]
%
% Note: the input to this function must be symmetric, so this function
% ignores the 'notrans' default option and never transposes the input.
%
% Example:
%    load graphs/clr-24-1.mat
%    mst(A)
%
% See also PRIM_MST, KRUSKAL_MST


%
% 2006-05-03: Changed to using kruskal as the default following problems
% with prim due to negative edge weights.
% 2006-05-31: Added full2sparse option
% 2006-06-15: Fixed error with graph symmetric (T+T') instead of max(T,T')
% found by Mark Cummins
% 2006-11-09: Temporary fix for disconnected graphs and the number of edges
% in the mst is LESS than n-1.
% 2006-11-10: Added warning for prim with disconnected graphs.
% 2007-04-09: Fixed documentation typos.  (Thanks Chris Maes.)
%



[trans check full2sparse] = get_matlab_bgl_options(varargin{:});
if (full2sparse && ~issparse(A)) 
    A = sparse(A); 
end

if (trans)
end;

options = struct('algname', 'kruskal');
if (length(varargin) > 0)
    options = merge_structs(varargin{1}, options);
end;

if (check)
    % make sure the matrix is symmetric
    check_matlab_bgl(A,struct('sym',1,'values',1,...
        'noneg', strcmp(options.algname,'prim')));
    
    if strcmp(options.algname,'prim')
        if max(components(A)) > 1
            warning('mst:connected', ...
                ['The output from MST using Prim''s algorithm\n' ...
                 'on a disconnected graph is only a partial spanning tree.']);
        end
    end
end;

% old temporary fix for incorrect number of edges
% num_components = max(components(A));

[i j v] = mst_mex(A,lower(options.algname));

% old temporary fix for disconnected graphs
% if (num_components > 1)
%     i = i(1:end-(num_components-1));
%     j = j(1:end-(num_components-1));
%     v = v(1:end-(num_components-1));
% end

if (nargout == 1 || nargout == 0)
    T = sparse(i,j,v,size(A,1),size(A,1));
    T = T + T';
    out1 = T;
else
    out1 = i; 
    out2 = j;
    out3 = v;
end;





