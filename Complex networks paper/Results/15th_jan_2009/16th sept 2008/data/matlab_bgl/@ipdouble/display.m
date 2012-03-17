function display(ipd)
% IPDOUBLE/DISPLAY Display an inplace double from the command line.
%
% Example:
%    ipd = ipdouble(ones(5));
%    ipd

disp([inputname(1), ' = ']);
disp(ipd.a);