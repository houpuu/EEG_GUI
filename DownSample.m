function output=DownSample(input,sample_ratio)
[channel,length]=size(input);
M=fix(length/400)*400;
N=fix(M/sample_ratio);
output=zeros(channel,M);
for i=1:sample_ratio
    output(:,(i-1)*N+1:i*N)=input(:,i:sample_ratio:M);
end


