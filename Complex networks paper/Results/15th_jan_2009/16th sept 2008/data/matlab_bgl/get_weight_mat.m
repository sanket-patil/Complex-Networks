function [weight_mat]= get_weight_mat(adj_mat,weight_information)


for i = 1 : length(adj_mat) - 1
    for j = 1 : length(adj_mat) -1 
        if(adj_mat{i+1, j+1} ~=0)
           
            node1 = adj_mat{j+1,1}; 
            
            node2 = adj_mat{i+1,1}; 
            
            for k = 1 : length(weight_information)
               if (strcmp(node1,weight_information{k,1}))
                   
                   lat1 = weight_information{k,2}; 
                   lon1 = weight_information{k,3}; 
                   
                   break; 
               end
               
            end
            
            for k = 1 : length(weight_information)
               if (strcmp(node2,weight_information{k,1}))
                   
                   lat2 = weight_information{k,2}; 
                   lon2 = weight_information{k,3}; 
                   break; 
                   
               end
               
            end
            
            d = acos(sin(lat1/57.2958)*sin(lat2/57.2958) + cos(lat1/57.2958)	*   cos(lat2/57.2958)*cos((lon1-lon2)/57.2958));



            nm = round(3437.747*d);
            
            weight = round(nm*1.13636);
            
            weight_mat(i,j) = weight; 
            
        else
            weight_mat(i,j) = 0; 
            
        end
    
    end 
    i
    pause(0.00001);
end

