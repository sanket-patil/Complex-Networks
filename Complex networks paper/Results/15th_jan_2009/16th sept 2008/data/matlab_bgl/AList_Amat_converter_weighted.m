% This is code for converting an adjacency list to an adjacency matrix.

% Written by Narendra Sharma June, 19, 2008



function [AMat]=AList_Amat_converter_weighted(Elist)



N=max(max(Elist(:,1)),max(Elist(:,2)));



AMat=zeros(N); % to initialize the square matrix (NXN) with all zeroes. 

for i=1:length(Elist(:,1))

    AMat(Elist(i,1), Elist(i,2))=Elist(i,3)/max(Elist(:,3));

  %  AMat(Elist(i,2), Elist(i,1))=1;

end

    
% fid = fopen('foodweb-1.txt', 'a'); 
% 
% for i = 1 : N
%     for j = 1 : N 
%         
%         fprintf(fid, '%4.7f \n',AMat(i,j)); 
%         
%     end 
%     
%     fprintf(fid, '\n'); 
% end 
% 
% fclose(fid); 


