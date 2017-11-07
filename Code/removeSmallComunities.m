a = [
    1
    2
    4
    5
    6
    7
    8
    8
     ];
 
 b = [
    2
    3
    6
    6
    7
    8
    9
    10
     ];
 
W = adjacency(graph(a, b));
plot(graph(W));
dim = size(W);
dim = dim(1);
 
deleted = 0;
max = 0;
maxi = 1;
d = []
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
        maxi = i - deleted; %initialization node
        max = s;
    end
end
Dh = diag(d.^(-1')); %to apply a random walk and remove those not touched

dim = size(W);
dim = dim(1);
p = zeros(dim, 1);
p(maxi) = 1;
pfinal = zeros(dim, 1);
pfinal(maxi) = 1;
for i = 1:300
    p = (Dh*W)*pfinal;
    pfinal(find(p)) = 1
end

graphPlot(W, p);