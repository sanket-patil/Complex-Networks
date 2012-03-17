function [varargout] = size(ipd)
% IPDOUBLE/SIZE Size of array
%
% [m,n] = size(ipd) Juse like SIZE for matrices and vectors.
%
% Example:
%    ipd = ipdouble(ones(10,3));
%    size(ipd)

varargout{:} = size(ipd.a);