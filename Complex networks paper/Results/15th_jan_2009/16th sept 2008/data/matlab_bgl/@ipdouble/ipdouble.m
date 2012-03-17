function ipd = ipdouble(a)
% IPDOUBLE Create a double type that supports inplace modification
% ipd = ipdouble(v) creates an inplace double object from any double
% matrix v.
%
% Example:
%    ipd = ipdouble(ones(5));

if nargin == 0
    error('ipdouble:invalidParameter', ['ipdouble must be created with '...
        'an initial matrix or vector.']);
elseif isa(a,'ipdouble')
    % make a copy
    ipd = ipdouble(a.a);
elseif isa(a,'double')
    if (ndims(a) > 2)
        error('ipdouble:invalidParameter', ...
            'Only matrices supported right now.');
    end;
    
    ipd.a = a;
    ipd = class(ipd,'ipdouble');
    
else
    error('ipdouble:invalidParameter', ['ipdouble must be created with '...
        'an initial double matrix or vector.']);
end;

