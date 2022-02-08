function output=sliding_window(x,sample_L,slide_L,ratio)
%1，滑窗得到M*2000*16的样本；
%2，下采样，得到M*400*16的样本；
[channel,L_raw]=size(x);
 M=fix((L_raw-sample_L)/slide_L)+1;
 output=zeros(M,sample_L/ratio,channel);
 for i=1:M
     x1=x(:,(i-1)*slide_L+1:(i-1)*slide_L+sample_L)';
     output(i,:,:)=x1(1:5:end,:);
 end