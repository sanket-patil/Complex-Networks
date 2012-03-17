function yn = isconnected(g)
% isconnected(g) -- determine if g is a connected graph
% Dan Whitney

% g = g+0.;
n = length(g);

x = zeros(n,1);
x(1)=1;

while(1)
     y = x;
     x = g*x + x;
     x = x>0;
     if (x==y)
         break
     end
end

if (sum(x)<n)
     yn = 0;
else
     yn = 1;
end
