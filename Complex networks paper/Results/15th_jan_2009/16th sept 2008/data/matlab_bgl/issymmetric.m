% Checks whether a matrix is symmetric
% Gergana Bounova, March 14, 2005

function [issym] = issymmetric(mat)

% inputs: (square) matrix
% outputs: boolean variable, {0,1}

% check whether mat=mat^T
issym = false; % default
if mat == transpose(mat)
  issym = true; return
end

