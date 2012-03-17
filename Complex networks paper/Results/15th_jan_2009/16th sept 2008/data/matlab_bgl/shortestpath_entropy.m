function [log_freq] = shortestpath_entropy(AList)

adj_mat = AList_Amat_converter(AList);

sparse_mat = sparse(adj_mat);

all_path = graphallshortestpaths(sparse_mat);

for i = 1 : length(all_path)
    for j = 1 : length(all_path)

        if (all_path(i,j) == Inf)

            all_path(i,j) = 0;

        end
    end
end

temp = [];

for i = 1 : length(all_path)
    
    for j = 1 : length(all_path)
           


        if (all_path(i,j)~=0)

            
                temp(length(temp)+1) = all_path(i, j);
            
        end
    end
end

count = 0; 

p=0;

for i = 1 : length(temp)
    
    if(temp(i) ~=0)
        
        p = p + 1; 
        
        count(p + 1) = 0;
        
        for j = 1 : length(temp)

            if (temp(i) == temp(j))

                count(p) =  count(p) + 1;
                
                if ( j ~= i)
                
                    temp(j) = 0;
                
                end
            end
        end

        temp(i) = 0;
        
     
        
    end
    
end
sum = 0; 

count(length(count)) = [];

for k = 1 : length(count) 
    
   sum = sum + count(k);  

end

for t = 1 : length(count)
    
    freq_eval(t) = count(t)/sum;  
    
end 
log_freq = 0;

for p = 1: length(freq_eval) 
    
   log_freq = log_freq - (freq_eval(p)*log(freq_eval(p))); 
   
   %fprintf('the log value: %1.4f \n',log_freq); 
   
   
end
%fprintf('the log value finally: %1.4f \n',log_freq); 

