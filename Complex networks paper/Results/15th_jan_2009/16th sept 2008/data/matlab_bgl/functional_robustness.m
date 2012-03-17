function [avg_case_fr, worst_case_fr] = functional_robustness(adj_matrix)

case_fr = 0;

temp=0;
local_matrix = adj_matrix;


func_robust(length(adj_matrix)) = 0;


for i = 1 : length(adj_matrix)

    clear node_num;
    clear temp_mat;
    clear new_adj_mat;
    clear new_sparse_mat;
    clear largest_comp;
    clear distance;
    clear local_matrix;
    clear n_hood;
    clear avg_path_length;
    
    norm_eff = 0;
local_matrix = adj_matrix;

    %     new_adj_mat = 0;
    
    n_hood = [];
     

    for r = 1 : length(adj_matrix)
        if (adj_matrix(i,r)~=0)
            n_hood(length(n_hood)+1) = r;
        
        elseif(adj_matrix(r,i)~=0)
            n_hood(length(n_hood)+1) = r;
        end
    end
   
    local_matrix(i,:) = 0;

    local_matrix(:,i) = 0;

    local_sparse_mat = sparse(local_matrix);
    
    array_graph = cell(length(n_hood));
    
    for c = 1 : length(n_hood)
        array_graph{c}= graphtraverse(local_sparse_mat, n_hood(c));
    end
  

    node_num(length(array_graph)) = 0; 
    
    for b = 1 : length(array_graph)
        
        temp_mat = array_graph{b};
        
        for q = 1 : length(temp_mat)

            for p = 1 : length(adj_matrix)
                
                if (temp_mat(q) ==p)
                    
                    node_num(b) = node_num(b) + 1; 
                    
                end

            end
        end

       
    end
    
    
    [value,index] = max(node_num); 

    largest_comp = array_graph{index}; 
    
%     fprintf('the largest_comp is %d \n',largest_comp); 
    
    for p = 1 : (length(largest_comp))
        
        for q = 1 : length(largest_comp)
        
      
        new_adj_mat(p,q) =0;
        
      
        end
    end
    
    
    for p = 1 : (length(largest_comp))
        
        for q = 1 : length(largest_comp)
            %         new_adj_mat(p,q) =local_matrix(largest_comp(p),largest_comp(q));
            if largest_comp(p)>i && largest_comp(q)>i
            new_adj_mat(largest_comp(p)-1,largest_comp(q)-1) =adj_matrix(largest_comp(p),largest_comp(q));
        
            elseif largest_comp(p)<i && largest_comp(q)>i
            new_adj_mat(largest_comp(p),largest_comp(q)-1) =adj_matrix(largest_comp(p),largest_comp(q));
       
            elseif largest_comp(p)>i && largest_comp(q)<i
            new_adj_mat(largest_comp(p)-1,largest_comp(q)) =adj_matrix(largest_comp(p),largest_comp(q));
       
            else
            new_adj_mat(largest_comp(p),largest_comp(q)) =adj_matrix(largest_comp(p),largest_comp(q));
            end
        end
    end
        

    
 
%     fprintf('the new adj_mat is %d \n',new_adj_mat);


    new_sparse_mat = sparse(new_adj_mat); 
    
    distance = graphallshortestpaths(new_sparse_mat); 
    
    temp_sum = 0; 
    
    for p = 1 : length(distance) 
        
        for q = 1 : length(distance) 
            
            temp_sum = temp_sum + distance(p,q); 
            
        end 
    end
   
    
    avg_path_length = temp_sum/(length(new_adj_mat)*(length(new_adj_mat)-1));
    
    if temp_sum == 0
        avg_path_length = Inf; 
        temp=temp+1;
    end

    star_avg_path_length = (2*(length(new_adj_mat)-1))/length(new_adj_mat);
    
    norm_eff = star_avg_path_length/avg_path_length; 

   
%     fprintf('the value of normalized eff. is %4.4f     \n',norm_eff);

    func_robust(i) = norm_eff;

    local_matrix = adj_matrix;
%     i
%     pause(0.001);
end

for k = 1 : length(adj_matrix)

    case_fr = case_fr + func_robust(k);

end

avg_case_fr = case_fr/length(adj_matrix);

worst_case_fr = min(func_robust);

fprintf('the avg_case_fr is: %4.4f \n',avg_case_fr); 
fprintf('the worst_case_fr is: %4.4f \n',worst_case_fr); 
