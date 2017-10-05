clear;
load Data/b.txt;
load Data/a.txt
W = adjacency(graph(a, b));

%{
W = [
     0     1     1     0     0     0     0     0     0     0
     1     0     1     1     0     0     0     0     0     0
     1     1     0     0     0     0     0     0     0     0
     0     1     0     0     1     0     1     0     0     0
     0     0     0     1     0     1     1     0     0     0
     0     0     0     0     1     0     1     0     0     0
     0     0     0     1     1     1     0     0     1     0
     0     0     0     0     0     0     0     0     1     1
     0     0     0     0     0     0     1     1     0     1
     0     0     0     0     0     0     0     1     1     0
     ];
%}

dim = size(W);
dim = dim(1)

%Degree of the nodes
deleted = 0;
max = 0;
maxi = 1;
for i=1:dim
    s = sum(W(i-deleted,:));
    if s == 0
        %we need to eliminate this no since it has no connections
        W(i-deleted,:) = [];
        W(:,i-deleted) = [];
        deleted = deleted + 1;
    else
        d(i-deleted) = s;
    end
    if s > max
        maxi = i - deleted;
        max = s;
    end
end
Dh = diag(d.^(-1/2)');

dim = size(W);
dim = dim(1)

%Original position of random walker
p = zeros(dim, 1);
p(maxi) = 100;
pz = p;

a = 0.99;
for i = 1:200
    p = a*(Dh*W*Dh)*p + (1-a)*pz;
end
p(maxi) = 0;
graphPlot(W, p);
