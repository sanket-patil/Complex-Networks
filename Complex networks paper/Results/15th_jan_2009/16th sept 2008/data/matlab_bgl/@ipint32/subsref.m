function b = subsref(ipi,index)
% IPINT32/SUBSREF Support Matlab subscript references.
%
% This function supports subscript references just like Matlab matrices.
%
% Example:
%    ipi = ipint32(int32(cumsum(ones(5,1))));
%    ipi([2 4])
    
if (length(index) > 1)
    error('Indexing operation not supported');
end;
if (strcmp(index.type,'()'))
    b = subsref(ipi.a,index);
elseif (strcmp(index.type,'.'))
    try
        a = 1;
        a.a;
    catch
        rethrow(lasterr);
    end;
elseif (strcmp(index.type,'{}'))
    try
        a = 1;
        a{1};
    catch
        rethrow(lasterr);
    end;
else
    error('Unsupported');
end;
