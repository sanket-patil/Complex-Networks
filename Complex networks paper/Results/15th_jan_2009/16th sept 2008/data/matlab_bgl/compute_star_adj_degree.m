
function [star_adj_mat_degree] = compute_star_adj_degree(adj_mat)
%STAR_DEGREE_CENTROID Summary of this function goes here

adj=adj_mat;

adj(1,:)=[];
adj(:,1)=[];

adj=cell2mat(adj);

% for j = 1 : length(adj_mat) -1
%     node1 = adj_mat(j+1,1); 
%     for k = 1 : length(weight_information)
%         if (strcmp(node1,weight_information(k,1)))
%             lat = weight_information{k,2}; 
%             x(j+1)=69.1*lat;
%             lon = weight_information{k,3}; 
%             y(j+1)= 53*lon;
%             break; 
%         end
%     end
% end

% x=x(2:length(adj_mat));
% y=y(2:length(adj_mat));

deg_seq=degrees_seq(adj);

[value, centre]= max(deg_seq);

% x_cent=x(centre);
% y_cent=y(centre);


star_adj_mat_degree=adj_mat;

for i=2:length(adj_mat)
    for j=2:length(adj_mat)
        star_adj_mat_degree{i,j}=0;
    end
end

for i=2:length(adj_mat)
    star_adj_mat_degree{i,centre}=1;
    star_adj_mat_degree{centre,i}=1;
end

star_adj_mat_degree{centre,centre}=0;

% 
% for i = 1:length(adj_mat) - 1
%     star_dist(i) = sqrt( (x(i)-x_cent)^2 + (y(i)-y_cent)^2 );
% end
% 
% 
% star_eff= 2*sum(star_dist)/length(adj)/(length(adj) - 1)/max(star_dist);
