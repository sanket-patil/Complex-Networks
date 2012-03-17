% This is code for converting an adjacency set to an adjacency matrix.

% Written by Leaelaf Hailemariam October 20, 2006



function [AMat]=ASet_Amat_converter(ESet);



N=max(max(ESet));



AMat=zeros(N);

for i=1:length(ESet(:,1))

    for j=2:length(ESet(1,:))

        if (ESet(i,j)>0)

            AMat(ESet(i,1), ESet(i,j))=1;

        end;

    end

end