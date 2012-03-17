% This is code for converting an adjacency list to an adjacency matrix.

% Written by Leaelaf Hailemariam October 17, 2006



function [AMat]=AList_Amat_converter(Elist)



N=max(max(Elist(:,1)),max(Elist(:,2)));



AMat=zeros(N); % to initialize the square matrix (NXN) with all zeroes. 

for i=1:length(Elist(:,1))

    AMat(Elist(i,1), Elist(i,2))=1;

  %  AMat(Elist(i,2), Elist(i,1))=1;

end

    



