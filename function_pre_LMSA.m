function new_x=function_pre_LMSA(x1)

M=5;
miu=0.02;
iter=201;

load('base_line.mat');
x_b=x(1,1:iter)/30;

x1(:,1:50)=0;
limit_x=size(x1,2)-201:size(x1,2);
x1(:,limit_x)=0;

for channel=1:16
    
    [max_x,index]=max(abs(x1(channel,:)));
 
    while  max_x>500 & index<limit_x
 
        x0=x1(channel,index-50:index+150);
        [d_est]=function_LMSA(x_b,x0,M,miu,iter);
        x1(channel,index-50:index+150)=d_est;
        [max_x,index]=max(abs(x1(channel,:)));
    end
        new_x(channel,:)=x1(channel,51:size(x1,2)-150);

end
    
