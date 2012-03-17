adj_1=adj;
    adj_1(1,:)=[];
    adj_1(:,1)=[];

for i= 1: length(adj)-1
%     clear adj_temp
    adj_2=adj_1;
    adj_2(i,:)=[];
    adj_2(:,i)=[];
    adj_temp=cell2mat(adj_2);
    [num_components(i),which_component]=graphconncomp(sparse(adj_temp),'directed',true);
end