function ipi = ipint32(a)
% IPINT32 Create an int32 type that supports inplace modification
% ipd = ipdouble(v) creates an inplace double object from any double
% matrix v.
%
% Example:
%    ipi = ipint32(int32(cumsum(ones(5,1))));

if nargin == 0
    error('ipint32:invalidParameter', ['ipint32 must be created with '...
        'an initial matrix or vector.']);
elseif isa(a,'ipint32')
    % make a copy
    ipi = ipint32(a.a);
elseif isa(a,'int32')
    if (ndims(a) > 2)
        error('ipint32:invalidParameter', ...
            'Only matrices supported right now.');
    end;
    
    ipi.a = a;
    ipi = class(ipi,'ipint32');
    
else
    error('ipint32:invalidParameter', ['ipint32 must be created with '...
        'an initial int32 matrix or vector.']);
end;

