function[] = computegraphproperties(adj_mat, weight_information)

for i=1:length(adj_mat)
    adj_mat{1,i}= adj_mat{i,1};
end


%complete graph
com_adj_mat = cell(length(adj_mat));

for i = 2 : length(adj_mat) 
    for j = 2 : length(adj_mat)  
        
        com_adj_mat{i,j} = 1;
    end
end

com_adj_mat(:,1) = adj_mat(:,1); 
com_adj_mat(1,:) = adj_mat(1,:);



% % % % com_weight_mat=get_weight_mat(com_adj_mat,weight_information);
% % % % 
% % % % sparse_com_mat = sparse(com_weight_mat);

weight_mat=get_weight_mat(adj_mat,weight_information);

sparse_mat = sparse(weight_mat); 

star_adj_mat_centroid= compute_star_adj_centriod(adj_mat,weight_information);

star_weight_mat_centroid=get_weight_mat(star_adj_mat_centroid,weight_information);

sparse_star_mat_centroid=sparse(star_weight_mat_centroid);

star_adj_mat_degree=compute_star_adj_degree(adj_mat);

star_weight_mat_degree=get_weight_mat(star_adj_mat_degree,weight_information);

sparse_star_mat_degree=sparse(star_weight_mat_degree);

adj_mat_1=adj_mat;
adj_mat_1(:,1) = []; 
adj_mat_1(1,:) = []; 

adj_matrix = cell2mat(adj_mat_1); 

sparse_matrix=sparse(adj_matrix);

noOfnodes = num_vertices(sparse_matrix); 

noOfedges = num_edges(sparse_matrix); 

apwsp = all_shortest_paths(sparse_mat,struct('algname','floyd_warshall'));

% % % % com_apwsp = all_shortest_paths(sparse_com_mat,struct('algname','floyd_warshall'));

star_apwsp_centroid = all_shortest_paths(sparse_star_mat_centroid,struct('algname','floyd_warshall'));

star_apwsp_degree = all_shortest_paths(sparse_star_mat_degree,struct('algname','floyd_warshall'));

fprintf('The number of nodes is: %d \n',noOfnodes);

fprintf('The number of edges is: %d \n',noOfedges);

connectance = noOfedges/(noOfnodes*(noOfnodes - 1));

fprintf('The Connectance is: %3.3f \n',connectance); 

apl = sum(sum(apwsp))/(noOfnodes*(noOfnodes - 1)); 

fprintf('The average path length is: %3.3f \n', apl); 

eff_secon = 1/apl; 

fprintf('The efficiency (as given in SECON paper) is: %1.3f \n',eff_secon); 

star_apl_centroid = sum(sum(star_apwsp_centroid))/(noOfnodes*(noOfnodes - 1)); 

fprintf('The average path length of star(centroid) is: %3.3f \n', star_apl_centroid); 

star_centroid_eff_norm= star_apl_centroid/apl;

fprintf('The efficiency normlized wrt star(centroid) is: %1.3f \n',star_centroid_eff_norm); 

star_apl_degree = sum(sum(star_apwsp_degree))/(noOfnodes*(noOfnodes - 1)); 

fprintf('The average path length of star(degree) is: %3.3f \n', star_apl_degree); 

star_degree_eff_norm= star_apl_degree/apl;

fprintf('The efficiency normlized wrt star(degree) is: %1.3f \n',star_degree_eff_norm); 


% % % com_apl = sum(sum(com_apwsp))/(noOfnodes*(noOfnodes - 1)); 

% % % fprintf('The average path length of complete graph is: %3.3f \n', com_apl); 

% % % % com_eff_norm = com_apl/apl;

% % % % fprintf('The efficiency normlized wrt complete graph is: %1.3f \n',com_eff_norm);

bc = betweenness_centrality(sparse_mat); 

norm_bc = bc/sum(bc);

highest_bc = max(norm_bc); 

fprintf('The highest node centrality is: %3.3f \n',highest_bc);

mean_bc = mean(norm_bc); 

fprintf('The mean node centrality is: %3.3f \n',mean_bc);

maxSkew = 1 - 1/noOfnodes;

skew = highest_bc - mean_bc;

robustness = (maxSkew - skew)/maxSkew;

fprintf('The value of Robustness is: %3.3f \n', robustness); 

% % % % beta_com = robustness/(com_eff_norm + robustness); 
% % % % 
% % % % fprintf('The value of beta(complete) is: %3.3f \n',beta_com); 

beta_star_centroid = robustness/(star_centroid_eff_norm + robustness); 

fprintf('The value of beta(star) is: %4.4f \n',beta_star_centroid); 

beta_star_degree = robustness/(star_degree_eff_norm + robustness); 

fprintf('The value of beta(star) is: %4.4f \n',beta_star_degree); 






% norm_bc = bc/((noOfnodes-1)*(noOfnodes - 2)); 
% norm_bc=bc;

% fprintf('The betweenness centrality is: %3.3f \n',bc);

% fprintf('The normalized betweenness centrality is: %3.3f \n',norm_bc);

% for i = 1 : length(apwsp)
%     for j = 1 : length(apwsp) 
%         
%         fprintf('The apwsp is: %d,  %d,  %d \n',apwsp(i,j),i,j);
%     end 
% end

% apwsp = graphallshortestpaths(sparse_mat); 
% temp_sparse = sparse(adj_matrix); 

% com_max_weight = max(max(com_weight_mat)); 
% 
% 
% for i = 1 : length(com_weight_mat) 
%     for j = 1 : length(com_weight_mat)
%         
%     
%         com_weight_mat(i,j) = com_weight_mat(i,j)/com_max_weight;
%    
%     end
% end
% 




% max_weight = max(max(weight_mat)); 
% 
% fprintf('The maximum weight is: %d \n',max_weight); 
% 
% 
% 
% 
% for i = 1 : length(weight_mat) 
%     for j = 1 : length(weight_mat)
%         
%     
%         weight_mat(i,j) = weight_mat(i,j)/max_weight;
%     
%     
%         if(weight_mat(i,j) == 0 & i ~= j) 
%        
%             weight_mat(i,j) = 0; 
%        
%     
%         end
% 
%     end
% end
% 













