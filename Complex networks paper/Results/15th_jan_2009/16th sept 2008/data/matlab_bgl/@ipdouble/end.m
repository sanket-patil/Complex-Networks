function n=end(ipd,a,n)
% IPDOUBLE/END Allow inline "end" indices to work.
%
% n=end(ipd,a,n) Returns the ending index along dimension a.
%
% Example:
%    ipd = ipdouble(cumsum(ones(5,1)));
%    ipd(3:end)

n = size(ipd.a,a);