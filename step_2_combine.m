close all
clear all
clc

%���������
file_name1='C:\EEG\eeg_DATA\shmtulab_seed\cnn_Sample';
%�²����任�����������
file_name2='C:\EEG\eeg_DATA\shmtulab_seed\cnn_Sample\dSample.mat';
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
    x=[x;train_input];
    y=[y;train_output];
     
end

train_input=x;
train_output=y;
save(file_name2,'train_input','train_output');