function d = double(ipd)
% IPDOUBLE/DOUBLE Return the data as a Matlab double type.  
% d = double(ipd) returns a double array.  Changing d will not change the
% ipd data.
%
% Example:
%    ipd = ipdouble(cumsum(ones(5,1)));
%    d = double(ipd);
%    d(2) = 10: % Doesn't change ipd

d = ipd.a;