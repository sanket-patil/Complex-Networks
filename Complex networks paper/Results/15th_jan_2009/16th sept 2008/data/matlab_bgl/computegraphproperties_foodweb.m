function[] = computegraphproperties_foodweb(weight_adj_list)

max_weight = max(weight_adj_list(:,3)); 

weight_adj_mat = AList_Amat_converter_weighted(weight_adj_list); 

 
sparse_mat = sparse(weight_adj_mat); 



noOfnodes = num_vertices(sparse_mat); 

noOfedges = num_edges(sparse_mat); 

apwsp = graphallshortestpaths(sparse_mat,'Directed',true); 

%fprintf('%d \n',apwsp);

for i = 1 : length(apwsp) 
    for j = 1 : length(apwsp) 
       if(apwsp(i,j) == Inf)
          apwsp(i,j) = 0;  
       end
        
    end 
end
%apwsp = all_shortest_paths(sparse_mat,struct('algname','auto'));


fprintf('The number of nodes is: %d \n',noOfnodes);

fprintf('The number of edges is: %d \n',noOfedges);

connectance = noOfedges/(noOfnodes*(noOfnodes - 1));

fprintf('The Connectance is: %3.3f \n',connectance); 

% for i = 1 : length(apwsp)
%     for j = 1 : length(apwsp) 
%         
%         fprintf('The apwsp is: %d,  %d,  %d \n',apwsp(i,j),i,j);
%     end 
% end
bc = betweenness_centrality(sparse_mat); 


%Type I normalizing.

%norm_bc = bc/((noOfnodes-1)*(noOfnodes - 2)); 

%Type II normalizing

norm_bc = bc/sum(bc);

% fprintf('The betweenness centrality is: %1.3f \n',bc);

% fprintf('The normalized betweenness centrality is: %3.3f \n',norm_bc);

apl = sum(sum(apwsp))/(noOfnodes*(noOfnodes - 1)); 



% fprintf('The average path length is: %3.3f \n', apl*max_weight); 


highest_bc = max(norm_bc); 

mean_bc = mean(norm_bc); 



% fprintf('The highest node centrality is: %3.3f \n',highest_bc);
% 
% fprintf('The mean node centrality is: %3.3f \n',mean_bc);

maxSkew = 1 - 1/noOfnodes;
skew = highest_bc - mean_bc;

robustness = (maxSkew - skew)/maxSkew;

fprintf('The value of Robustness is: %3.3f \n', robustness); 















