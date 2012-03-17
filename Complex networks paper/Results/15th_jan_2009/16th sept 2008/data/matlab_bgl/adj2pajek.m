% Converts an adjacency matrix representation to a Pajek .net read format
% CAUTION: Before loading the .net file into Pajek, open, save and
% close it in WordPad. That fixes some strange UNIX-Win incompatibility
% Gergana Bounova, March 14, 2006

function []=adj2pajek(adj,filename,x,y,z)

% INPUT: an adjacency matrix, NxN, N - # nodes
%        a filename, string format

% OUTPUT: text format of Pajek readable net representation

% EXAMPLE
% *Vertices    4
%        1 "v1"                                     0.1000    0.5000    0.5000
%        2 "v2"                                     0.1000    0.4975    0.5000
%        3 "v3"                                     0.1000    0.4950    0.5000
%        4 "v4"                                     0.1001    0.4925    0.5000
% *Edges
%       14       31 1 
%       46       51 1 
%       51       60 1 

N = length(adj); % number of nodes
  
fid = fopen(filename,'w','native');

fprintf(fid,'*Vertices  %6i\n',N);
if nargin < 3
  for i=1:N
    fprintf(fid,'     %3i %s                     %1.4f    %1.4f   %1.4f\n',i,strcat('"v',num2str(i),'"'),rand,rand,0.5);
  end
elseif nargin >2 & nargin < 5
  for i=1:N
    fprintf(fid,'     %3i %s                     %1.4f    %1.4f   %1.4f\n',i,strcat('"v',num2str(i),'"'),x(i),y(i),0.5);
  end
else % 3D coords
  for i=1:N
    fprintf(fid,'     %3i %s                     %1.4f    %1.4f   %1.4f\n',i,strcat('"v',num2str(i),'"'),x(i),y(i),z(i));
  end
end

fprintf(fid,'*Edges\n');
for i=1:N
  for j=1:N
    if adj(i,j)>0
      fprintf(fid,'    %4i   %4i   %2i\n',i,j,adj(i,j));
    end
  end
end

fclose(fid)