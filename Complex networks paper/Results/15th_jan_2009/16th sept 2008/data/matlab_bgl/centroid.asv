

for i = 1 : length(adj_mat) - 1
    for j = 1 : length(adj_mat) -1 
           
            node1 = adj_mat{1, j+1}; 
            
            
            
            for k = 1 : length(weight_information)
               if (strcmp(node1,weight_information{k,1}))
                   
                   lat = weight_information{k,2}; 
                   x(j+1)=69.1*lat;
                   lon = weight_information{k,3}; 
                   y(j+1)= 53*lon;
                   
                   break; 
               end
               
            end
    end
    i
    pause(0.0001);
end
x=x(2:length(adj_mat));
y=y(2:length(adj_mat));
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

for i = 1:length(adj_mat) - 1

star_dist(i) = sqrt( (x(i)-x(centre))^2 + (y(i)-y(centre))^2 );


end

star_eff= 2*sum(star_dist)/(length(adj_mat) - 1)/(length(adj_mat) - 2)/max(star_dist);
