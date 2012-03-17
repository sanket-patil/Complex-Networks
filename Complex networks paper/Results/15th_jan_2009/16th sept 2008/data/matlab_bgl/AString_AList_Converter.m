function [] = AString_AList_Converter(Estring)

% This is code for converting list of strings to an adjacency List.

% Written by Narendra Sharma March 30, 2008.


% N=size(Estring,1);



% Elist =zeros(N); % to initialize the square matrix (NXN) with all zeroes.


savefile2 = input('File Name for names: '); 


fid2 = fopen(savefile2, 'a'); 

value = 1;

name = []; 

for n = 1 : 2

    for m = 1 : size(Estring,1)

        if (ischar(Estring{m,n}))

            temp = Estring{m,n};

            name{length(name) + 1} = temp; 
            
            fprintf(fid2, '%s \n',temp); 
            
            for p = 1 : size(Estring,1)

                for q = 1:2


                    if(strcmp(temp,Estring{p,q}))

                        Estring{p,q} = value;
                    end


                end
            end

            value = value + 1;

        end
    end
end

Elist =zeros(value-1);

fprintf('the last value of value is %d \n', value);  

for i=1:size(Estring,1)

    Elist(Estring{i,1}, Estring{i,2})=1;

    %  AMat(Elist(i,2), Elist(i,1))=1;

end

savefile = input('File Name for adj mat: '); 

save(savefile, 'Elist');
% 
% savefile2 = input('File Name for names: '); 
% 
% save(savefile2, 'name');



fclose(fid2); 



