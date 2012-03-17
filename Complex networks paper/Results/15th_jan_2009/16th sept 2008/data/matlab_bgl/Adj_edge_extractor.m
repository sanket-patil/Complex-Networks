% This is a function that extracts a set of edges from an adjacency matrix:

% Written on September 20, 2006 by Leaelaf Hailemariam



function [list_of_edges]=Adj_edge_extractor(adj_matrix) 



Nspec=length(adj_matrix(:,1));

list_of_edges=zeros(sum(sum(adj_matrix)),3);

list_ctr=0;



for i=1:Nspec

    for j=1:Nspec

        if (adj_matrix(i,j)>0)

            list_ctr=list_ctr+1;

            list_of_edges(list_ctr,1)=i;

            list_of_edges(list_ctr,2)=j;

        end;

    end

end