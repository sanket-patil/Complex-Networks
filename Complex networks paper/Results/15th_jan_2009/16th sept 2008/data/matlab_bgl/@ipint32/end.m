function n=end(ipd,a,n)
% IPINT32/END Allows inline "end" indices to work.
%
% n=end(ipi,a,n) Returns the ending index along dimension a.
%
% Example:
%    ipi = ipint32(int32(cumsum(ones(5,1))));
%    ipi(3:end)

n = size(ipd.a,a);