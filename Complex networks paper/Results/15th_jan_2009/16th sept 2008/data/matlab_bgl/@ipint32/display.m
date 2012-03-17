function display(ipi)
% IPINT32/DISPLAY Display an inplace int32 from the command line
%
% Example:
%    ipi = ipint32(int32(cumsum(ones(5,1))));
%    ipi

disp([inputname(1), ' = ']);
disp(ipi.a);