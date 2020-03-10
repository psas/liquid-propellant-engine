
% read xls files and get average values graphically
clear, close all, clc
% --- read data into cell array ---

files = dir('*.xls');
names = {files.name};
names = string(names');
endVal = size(names);
endVal = endVal(1);
data = cell(1,endVal)';

for ii = 1:endVal
data{ii} = xlsread(names(ii));
end

%%
% --- trim data ---
averages = zeros(endVal,2);
for ii = 1:endVal
plot(data{ii}(1:end,1),data{ii}(1:end,3))
title('choose P_{start}, P_{end}, noise_{start}, noise_{end}')
[x,y] = ginput(4);
% indices from ginput
% pressure
[val,p1] = min(abs(data{ii}(1:end,1)-x(1)));
[val,p2] = min(abs(data{ii}(1:end,1)-x(2)));
% noise
[val,n1] = min(abs(data{ii}(1:end,1)-x(3)));
[val,n2] = min(abs(data{ii}(1:end,1)-x(4)));
% average values
p_ave = mean(data{ii}(p1:p2,3));
n_ave = mean(data{ii}(n1:n2,3));
% put values into averages array
averages(ii,1) = p_ave;
averages(ii,2) = n_ave;
end


