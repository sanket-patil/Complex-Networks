% This program converts an adjacency matrix representation to an incidence
% matrix representation for an arbitrary network
% Valid for directed/undirected, simple/not simple graph
% Gergana Bounova, Last Updated: March 9, 2006

function [inc] = adj2inc(adj)

% INPUT
% adjacency matrix, NxN, N - number of nodes

% OUTPUT
% incidence matrix: N x number of edges

N = length(adj);

inc = zeros(N,num_edges(adj));
cnt = 0; % counting edges for the loop

if isdirected(adj)
  while not(isempty(find(adj>0)))
    new = find(adj>0); % find edges
    % get indeces of first edge
    x = mod(new(1),N);  
    if x==0
      x=N;
    end
    y = ceil(new(1)/N);
    cnt = cnt + 1;
    if x==y
      inc(x,cnt) = 0;
      fprintf('self loop at node %i\n',x)
      adj(x,x) = adj(x,x)-1;
    else
      inc(x,cnt) = -1; % assign new edge
      inc(y,cnt) = 1; 
      adj(x,y) = adj(x,y) - 1;
    end
  end
  
else % undirected graph
  while not(isempty(find(adj>0)))
    new = find(adj>0); % find edges
    % get indeces of first edge
    x = mod(new(1),N);  
    if x==0
      x=N;
    end
    y = ceil(new(1)/N);
    cnt = cnt + 1;
    if x==y
      inc(x,cnt) = inc(x,cnt)+1;
      adj(x,x) = adj(x,x)-1;
    else
      inc(x,cnt) = inc(x,cnt)+1; % assign new edge
      inc(y,cnt) = inc(y,cnt)+1; 
      adj(x,y) = adj(x,y) - 1;
      adj(y,x) = adj(y,x) - 1;
    end
  end
  
end

