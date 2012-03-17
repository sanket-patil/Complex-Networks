
function [star_eff] = compute_star_adj_degree(adj_mat,weight_information)
%STAR_DEGREE_CENTROID Summary of this function goes here

adj=adj_mat;

adj(1,:)=[];
adj(:,1)=[];

adj=cell2mat(adj);

for j = 1 : length(adj_mat) -1
    node1 = adj_mat(j+1,1); 
    for k = 1 : length(weight_information)
        if (strcmp(node1,weight_information(k,1)))
            lat = weight_information{k,2}; 
            x(j+1)=69.1*lat;
            lon = weight_information{k,3}; 
            y(j+1)= 53*lon;
            break; 
        end
    end
end

x=x(2:length(adj_mat));
y=y(2:length(adj_mat));

deg_seq=degrees_seq(adj);

[value, index]= max(deg_seq);

x_cent=x(index);
y_cent=y(index);

for i = 1:length(adj_mat) - 1
    star_dist(i) = sqrt( (x(i)-x_cent)^2 + (y(i)-y_cent)^2 );
end


star_eff= 2*sum(star_dist)/length(adj)/(length(adj) - 1)/max(star_dist);
