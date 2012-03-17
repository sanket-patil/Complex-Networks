function [varargout] = size(ipi)
% IPINT32/SIZE Size of array
%
% [m,n] = size(ipi) Just like SIZE for matrices and vectors.
%
% Example:
%    ipi = ipint32(int32(cumsum(ones(5,1))));
%    size(ipi)

%
% David Gleich
% 1 June 2006
%


varargout{:} = size(ipi.a);