% This is code written by Leaelaf Hailemariam to compute the Total (1/km)

% vs (1/C) ratios for different networks. Here, k is the number of prey a

% species has and m is the number of predators a species has. C is the

% connectance; defined by the ratio of the actual number of edges divided

% by the number of theoretical edges (n(n-1)). Written on May 12, 2007 at

% Purdue University. 



function [Tot_1_km]= Total_1_km_computer(adj_matrix);



%1. The first step is to convert the adjacency matrix into an adjacency

%list to find the relevant edges



clear list_of_edges;

list_of_edges = Adj_edge_extractor(adj_matrix);

N_spec=length(adj_matrix(1,:));



%2. The k and m values are computed by finding the number of prey



Predcount=zeros(N_spec,1);

Preycount=zeros(N_spec,1);



for i=1:N_spec

    Predcount(i)=sum(adj_matrix(:,i));

    Preycount(i)=sum(adj_matrix(i,:));

end



for k=1:length(list_of_edges(:,1))

    k_memb=list_of_edges(k,1);

    m_memb=list_of_edges(k,2);

    fprintf('\n Edge = [%1.0f %1.0f ]     Preycount = %1.0f  Predcount = %1.0f',k_memb,m_memb,Preycount(k_memb),Predcount(m_memb)) 

    list_of_edges(k,3)=1/(Preycount(k_memb)*Predcount(m_memb));

end;



Conn=length(list_of_edges(:,1))/(N_spec*(N_spec-1));

fprintf('\n\n The Connectance is: %1.4f \n',Conn);

Tot_1_km = sum(list_of_edges(:,3))*Conn;

fprintf('\n The Total(1/KM) value is: %1.4f \n',(Tot_1_km)/Conn);
fprintf('\n The Ratio of Total(1/KM) and Connectance is: %1.4f\n',Tot_1_km);





