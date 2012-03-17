% Checks whether a graph is directed 
% Gergana Bounova, February 19, 2006

function [isit] = isdirected(adj)

% INPUTs: adj - adjacency matrix
% OUTPUTs: isit - boolean variable

if adj==transpose(adj) % if it is symmetric
  isit = false; return
else  % not symmetric
  isit = true; return
end