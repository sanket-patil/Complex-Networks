function [star_adj_mat_centroid]= compute_star_adj_centriod(adj_mat, weight_information)

for i = 1 : length(adj_mat) - 1 

            for k = 1 : length(weight_information)
            
               if (strcmp(adj_mat(i+1, 1),weight_information(k,1)))
                   
                   lat = weight_information{k,2}; 
                   x(i)=69.1*lat;
                   
                   lon = weight_information{k,3}; 
                   y(i)= 53*lon;
                 
                   
                   
                   break; 
               end
            end
              

    i
    pause(0.0001);
end



x_cent=mean(x);
y_cent=mean(y);


for i = 1:length(adj_mat) - 1

dist_cent(i) = sqrt( (x(i)-x_cent)^2 + (y(i)-y_cent)^2 );


end

for i=1:length(adj_mat) - 1
    if dist_cent(i)== min(dist_cent)
        centre=i;
    end
end


star_adj_mat_centroid=adj_mat;

for i=2:length(adj_mat)
    for j=2:length(adj_mat)
        star_adj_mat_centroid{i,j}=0;
    end
end

for i=2:length(adj_mat)
star_adj_mat_centroid{i,centre}=1;
star_adj_mat_centroid{centre,i}=1;
end

star_adj_mat_centroid{centre,centre}=0;
