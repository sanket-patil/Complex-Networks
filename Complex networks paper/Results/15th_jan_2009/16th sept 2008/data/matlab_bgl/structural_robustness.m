function [avg_case_sr,worst_case_sr] = structural_robustness(adj_matrix)
 
case_sr = 0; 

local_matrix = adj_matrix; 

%sparse_mat = sparse(adj_matrix); 

%[S, C] = graphconncomp(sparse_mat); 


 

struct_robust(length(adj_matrix)) = 0; 


for i = 1 : length(adj_matrix) 
    
    eff_access = 0;
    
    local_matrix(i,:) = []; 
    
    local_matrix(:,i) = []; 
    
    local_sparse_mat = sparse(local_matrix); 
    
    [local_S, local_C] = graphconncomp(local_sparse_mat); 
    
    %,'Directed',false
    
    for t = 1 : local_S
        counter(t) = 0; 
    end
    
%     fprintf('the value of local_S and Local_C is %d \n',local_S); 
    
    for j = 1 : local_S
        
        for m = 1 : length(local_C)
            
            if (local_C(m) == j)
                
                counter(j) = counter(j) + 1; 
                
                
                
            end
        end
    end
%     fprintf('the value of counter is %d \n',counter);
    
    for n = 1 : local_S 
        
        eff_access = eff_access + (counter(n)-1); 
        
        
    end
    
%     fprintf('the value of effective access. is %4.2f \n',eff_access);
    
    struct_robust(i) = eff_access/(length(adj_matrix)-2); 
    
    local_matrix = adj_matrix; 

end

for k = 1 : length(adj_matrix)
    
case_sr = case_sr + struct_robust(k); 

end

avg_case_sr = case_sr/length(adj_matrix); 

worst_case_sr = min(struct_robust); 
fprintf('The avg_case_sr is: %1.4f \n',avg_case_sr);
fprintf('The worst_case_sr is %1.4f \n',worst_case_sr); 



