function d = double(ipi)
% IPINT32/DOUBLE Return the data as a Matlab double type.  
% d = double(ipi) returns a double array.  Changing d will not change the
% ipi data.
%
% Example:
%    ipi = ipint32(int32(cumsum(ones(5,1))));
%    d = double(ipi);
%    d(2) = 10;  % Doesn't change ipi

d = double(ipi.a);