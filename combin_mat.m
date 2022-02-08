close all
clear all
clc

%输入的数据
file_name1='C:\EEG\eeg_DATA\music\down_sample\excited';
%下采样变换后的样本保存
file_name2='C:\EEG\eeg_DATA\music\down_sample\excited\dexcited.mat';
input_option.type='dir';
input_option.ext='.mat';
pos_file_list=FileInput(file_name1,input_option);
length_data=length(pos_file_list.data);
x=[];
y=[];
%%
for k=1:length_data

    S_signalname=char(pos_file_list.data(1,k));
    load(S_signalname);
    x=[x;EEGdata];
     
end
train_input=x;
train_output=ones(;
save(file_name2,'train_input','train_output');