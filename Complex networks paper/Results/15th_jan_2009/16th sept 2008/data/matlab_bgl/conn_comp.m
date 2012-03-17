% Algorithm for finding connected components in a graph
% Gergana Bounova, December 4, 2005

function [conn,comp] = conn_comp(adj)

% input: adj - adjacency matrix of graph

% output: a linked list, comp(i).pts
%         conn = 0/1 -> graph isn't/is connected
%         if graph is connected, there are two components output,
%         [] and the entire graph

n = size(adj,1); % number of points
new_points = [1:n];
searched = [];
comp(1).pts = [];

while length(new_points)>0
  % pick a random point from new_points
  new_p = new_points(ceil(rand*numel(new_points))); old = 0;
  % check if it already belongs to a component
  for c=1:length(comp)
    for p=1:length(comp(c).pts)
      if shortest_pathDP(adj,new_p,comp(c).pts(p),n)<inf
    	comp(c).pts = [comp(c).pts new_p];
	    old = 1;
	    searched = [searched new_p];
	    new_points = setdiff(new_points,new_p);
        break
      end
    end
  end
  if not(old)
    comp(length(comp)+1).pts = [new_p];
    searched = [searched new_p];
    new_points = setdiff(new_points,new_p);
  end
%   for i=1:n
%     if adj(new_p,i)==1
%       comp(length(comp)).pts = [comp(length(comp)).pts i];
%       searched = [searched i];
%       new_points = setdiff(new_points,i);
%     end
%   end
  
end

if length(comp)>2
    conn = false;
    fprintf(strcat('graph not connected',', ',num2str(length(comp)-1),' connected components\n'));
else
    conn = true;
    'connected'
end