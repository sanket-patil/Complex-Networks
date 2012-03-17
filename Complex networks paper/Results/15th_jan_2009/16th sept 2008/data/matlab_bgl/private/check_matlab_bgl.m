function check_matlab_bgl(A,options)
% CHECK_MATLAB_BGL Checks the input A for various properties
%
% check_matlab_bgl(A,options) throws an input error if...
%   A is not square
%   if options.values and A is not double valued
%   if options.sym = 1 and A is not symmetric
%   if options.flow_graph = 1 and A is not a flow graph data structure
%   if options.nosparse = 1 do not check if A is sparse
%

if (size(A,1) ~= size(A,2))
    error('matlab_bgl:invalidParameter', 'the matrix A must be square.');
end;

if (isfield(options, 'values') && options.values == 1)
    if (~isa(A,'double'))
        error('matlab_bgl:invalidParameter', 'the matrix A must have double values.');
    end;
end;

if (isfield(options, 'noneg') && options.noneg == 1)
    if (min(min(A)) < 0)
        error('matlab_bgl:invalidParameter', 'the matrix A must have non-negative values.');
    end;
end;

if (isfield(options, 'sym') && options.sym == 1)
    if (~isequal(A,A'))
        error('matlab_bgl:invalidParameter', 'the matrix A must be symmetric.');
    end;
end;

if (isfield(options, 'nosparse') && options.nosparse == 1)
else
    if (~issparse(A))
        error('matlab_bgl:invalidParameter', 'the matrix A must be sparse.  (See set_matlab_bgl_default.)');
    end;
end;




