function[] = computegraphproperties_unweighted(adj_mat)

com_weight_mat = ones((length(adj_mat) )); 

com_sparse_mat = sparse(com_weight_mat);

adj_matrix=adj_mat;
% % % % % % adj_matrix(:,1) = []; 
% % % % % % adj_matrix(1,:) = []; 

% % % % % % adj_matrix = cell2mat(adj_matrix); 

temp_sparse = sparse(adj_matrix); 

sparse_mat = sparse(adj_matrix); 
      
noOfnodes = num_vertices(temp_sparse); 
noOfedges = num_edges(temp_sparse); 
fprintf('The number of nodes is: %d \n',noOfnodes);
fprintf('The number of edges is: %d \n',noOfedges);

connectance = noOfedges/(noOfnodes*(noOfnodes - 1));
fprintf('The Connectance is: %3.3f \n',connectance); 


apwsp = graphallshortestpaths(temp_sparse,'Directed',true); 
apl = sum(sum(apwsp))/(noOfnodes*(noOfnodes - 1)); 
fprintf('The average path length is: %3.3f \n', apl); 
eff_secon = 1/apl; 
fprintf('The efficiency (as given in SECON paper) is: %1.3f \n',eff_secon); 


com_apwsp = all_shortest_paths(com_sparse_mat,struct('algname','floyd_warshall'));
com_apl = sum(sum(com_apwsp))/(noOfnodes*(noOfnodes - 1)); 
fprintf('The average path length for complete graph is: %3.3f \n', com_apl); 
com_eff_norm = com_apl/apl;
fprintf('The efficiency normlized wrt complete graph is: %1.3f \n',com_eff_norm);

star_apl=(2 * (noOfnodes - 1)/noOfnodes);
star_eff_norm = star_apl/apl;
fprintf('The average path length for star graph is: %3.3f \n', star_apl); 
fprintf('The efficiency normlized wrt star graph is: %1.3f \n',star_eff_norm);



bc = betweenness_centrality(sparse_mat);
norm_bc = bc/sum(bc);
highest_bc = max(norm_bc); 
mean_bc = mean(norm_bc); 
fprintf('The highest node centrality is: %3.3f \n',highest_bc);
fprintf('The mean node centrality is: %3.3f \n',mean_bc);


maxSkew = 1 - 1/noOfnodes;
skew = highest_bc - mean_bc;
robustness = (maxSkew - skew)/maxSkew;
fprintf('The value of Robustness is: %3.3f \n', robustness); 


com_beta = robustness/(com_eff_norm + robustness); 
star_beta = robustness/(star_eff_norm + robustness); 
fprintf('The value of beta(complete graph) is: %3.3f \n',com_beta); 
fprintf('The value of beta(star) is: %3.3f \n',star_beta); 








% isone = sum(norm_bc); 
% fprintf('The value of summation of normalized betweenness centrality is: %d \n', isone); 

%complete graph
% com_adj = cell(length(adj_mat));
% 
% for i = 1 : length(adj_mat) - 1
%     for j = 1 : length(adj_mat) -1 
%         
%         com_adj{i,j} = 1;
%     end
% end
% 
% com_adj(:,1) = adj_mat(:,1); 
% com_adj(1,:) = adj_mat(1,:);
% 


% for i = 1 : length(com_adj) - 1
%     for j = 1 : length(com_adj) -1 
%            
%             node1 = com_adj{1, j+1}; 
%             
%             node2 = com_adj{i+1, 1}; 
%             
%             for k = 1 : length(weight_information)
%                if (strcmp(node1,weight_information{k,1}))
%                    
%                    lat1 = weight_information{k,2}; 
%                    lon1 = weight_information{k,3}; 
%                    
%                    break; 
%                end
%                
%             end
%             
%             for k = 1 : length(weight_information)
%                if (strcmp(node2,weight_information{k,1}))
%                    
%                    lat2 = weight_information{k,2}; 
%                    lon2 = weight_information{k,3}; 
%                    break; 
%                    
%                end
%                
%             end
%             
%             d = acos(sin(lat1/57.2958)*sin(lat2/57.2958) + cos(lat1/57.2958)	*   cos(lat2/57.2958)*cos((lon1-lon2)/57.2958));
% 
% 
% 
%             nm = round(3437.747*d);
%             
%             weight = round(nm*1.13636);
%             
%             com_weight_mat(i,j) = weight; 
%     
%     end 
% end
% 
% com_max_weight = max(max(com_weight_mat)); 


% for i = 1 : length(com_weight_mat) 
%     for j = 1 : length(com_weight_mat)
%         
%     
%         com_weight_mat(i,j) = com_weight_mat(i,j)/com_max_weight;
%    
%     end
% end









%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% radius_of_world = 3950; 
% 
% for i = 1 : length(adj_mat) - 1
%     for j = 1 : length(adj_mat) -1 
%         if(adj_mat{i+1, j+1} ~=0)
%            
%             node1 = adj_mat{1, j+1}; 
%             
%             node2 = adj_mat{i+1, 1}; 
%             
%             for k = 1 : length(weight_information)
%                if (strcmp(node1,weight_information{k,1}))
%                    
%                    lat1 = weight_information{k,2}; 
%                    lon1 = weight_information{k,3}; 
%              
%                    break; 
%                end
%                
%             end
%             
%             for k = 1 : length(weight_information)
%                if (strcmp(node2,weight_information{k,1}))
%                    
%                    lat2 = weight_information{k,2}; 
%                    lon2 = weight_information{k,3}; 
%                    
%                    x(i) = radius_of_world * cos(lon2/57.2958) * sin((90 - lat2)/57.2958); 
%                    y(i) = radius_of_world * sin(lon2/57.2958) * sin((90 - lat2)/57.2958);
%                    z(i) = radius_of_world * cos((90 - lat2)/57.2958);
%                    longitude(i) = lon2; 
%                    latitude(i) = lat2; 
%                    
%                    break; 
%                    
%                end
%                
%             end
%             
%             d = acos(sin(lat1/57.2958)*sin(lat2/57.2958) + cos(lat1/57.2958)	*   cos(lat2/57.2958)*cos((lon1-lon2)/57.2958));
% 
% 
% 
%             nm = round(3437.747*d);
%             
%             weight = round(nm*1.13636);
%             
%             weight_mat(i,j) = weight; 
%             
%         else
%             weight_mat(i,j) = 0; 
%             
%         end
%     
%     end 
% end
% 
% max_weight = max(max(weight_mat)); 

% fprintf('The maximum weight is: %d \n',max_weight); 


% mean_x = mean(x); 
% mean_y = mean(y); 
% mean_z = mean(z); 

% fprintf('%d, %d, %d \n', mean_x, mean_y, mean_z); 

% for i = 1 : length(x)
%    relative_dist(i) = sqrt((mean_x - x(i))^2 + (mean_y - y(i))^2 + (mean_z - z(i))^2); 
% end
% 
% [value, index] = min(relative_dist); 
% 
% % fprintf('value: %d, index: %d \n', value, index); 
% 
% distance_of_other_rel_min = weight_mat(index, :); 

% star_weight_mat = zeros(length(weight_mat)); 



% star_weight_mat(index, :) =  weight_mat(index, :); 
% 
% for i = 1 : length(weight_mat) 
%     
%     star_weight_mat(i, index) = weight_mat(index, i); 
% 
% end

% for i = 1 : length(weight_mat) 
%         
%         lon1 =  longitude(index); 
%         lat1 =  latitude(index); 
%         
%         lon2 = longitude(i); 
%         lat2 = latitude(i); 
%         
%         d = acos(sin(lat1/57.2958)*sin(lat2/57.2958) + cos(lat1/57.2958)	*   cos(lat2/57.2958)*cos((lon1-lon2)/57.2958));
% 
%         nm = round(3437.747*d);
%             
%         weight = round(nm*1.13636);
%         
%         star_weight_mat(i, index) = weight; 
%         star_weight_mat(index,i) = weight; 
%         
% end


% for i= 1 : length(star_weight_mat) 
%     for j = 1 : length(star_weight_mat) 
%         
%         fprintf('the weight between %d and %d is: %d \n', i, j, star_weight_mat(i,j));
%    
%     end 
%     
% end

% sparse_star_weight_mat = sparse(star_weight_mat); 


% for i = 1 : length(weight_mat) 
%     for j = 1 : length(weight_mat)
%         
%     
% %         weight_mat(i,j) = weight_mat(i,j)/max_weight;
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

 

% sparse_mat = sparse(weight_mat); 

% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% apwsp = graphallshortestpaths(sparse_mat); 



% star_apwsp = all_shortest_paths(sparse_star_weight_mat,struct('algname','floyd_warshall'));




% for i = 1 : length(apwsp)
%     for j = 1 : length(apwsp) 
%         
%         fprintf('The apwsp is: %d,  %d,  %d \n',apwsp(i,j),i,j);
%     end 
% end
 

%Type I normalizing.

%norm_bc = bc/((noOfnodes-1)*(noOfnodes - 2)); 

%Type II normalizing



% fprintf('The betweenness centrality is: %3.3f \n',bc);

% fprintf('The normalized betweenness centrality is: %3.3f \n',norm_bc);


% 
% for i = 1 : length(star_apwsp) 
%     for j = 1 : length(star_apwsp) 
% %         fprintf('%d', star_apwsp(i,j)); 
%         if(star_apwsp(i,j) == Inf)
%            star_apwsp(i,j) = 0;  
%         end
%     end 
% end
% star_apl = sum(sum(star_apwsp))/((noOfnodes-1)*(noOfnodes - 2)); 






