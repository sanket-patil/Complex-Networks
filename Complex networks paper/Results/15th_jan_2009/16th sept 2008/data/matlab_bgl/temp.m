for i=1:size(weight_adj_mat)
    for j=1:size(weight_adj_mat)
        if( weight_adj_mat(i,j)>0)
            adj_mat(i,j)=1;
        else 
            adj_mat(i,j)=0;
        end
    end
end

            