% Computes clustering coefficient, based on triangle motifs count
% Valid for directed and undirected graphs
% Gergana Bounova, May 2, 2006

function [C1,C2,C] = clust_coeff(adj)

% INPUT: adjacency matrix representation of a graph

% OUTPUT: graph average clustering coefficient and clustering coefficient
% per node

N = length(adj);
adj = adj > 0;
adj = str2num(num2str(adj));
[deg,indeg,outdeg] = degrees_seq(adj);

% find neighboring links
str = adj2str(adj);


if isdirected(adj)
    for i=1:N
        if outdeg(i)==1 | outdeg(i)==0
            C(i) = 0;
        else 
            count = 0;
            for s=1:outdeg(i)
                for t=s+1:outdeg(i)
                    if adj(str(i).child(s),str(i).child(t))>0
                        count = count + 1;
                    end 
                end
            end
            C(i) = count/(outdeg(i)*(outdeg(i)-1));
        end
    end
    
else   % undirected
    for i=1:N
        if deg(i)==1 | deg(i)==0
            C(i) = 0;
        else   
            count = 0;
            for s=1:deg(i)
                for t=s+1:deg(i)
                    if adj(str(i).child(s),str(i).child(t))>0
                        count = count + 1;
                    end 
                end
            end
            C(i) = 2*count/(deg(i)*(deg(i)-1));
        end
    end

end
C1 = sum(C(find(deg>1)))/numel(find(deg>1));
C2 = sum(C)/N;