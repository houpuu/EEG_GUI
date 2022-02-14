%% 
% 下采样到200HZ； 

%音乐诱发的数据，EEGdata;
%图片诱发的数据，分别是face(renlian),food(wucan),landscape(fengjing),
%...sick(exin),snake(she),spider(zhizhu)
%label:excited-4,happy-3,peace-2,sad-1,fear-0

%%
close all
clear all
clc

addpath('C:\EEG\eeg_function');

%输入的数据
file_name1='C:\EEG\eeg_DATA\shmtulab_seed\LSMA_zhou';
%下采样变换后的样本保存
file_name2='C:\EEG\eeg_DATA\shmtulab_seed\down_sample\zhou_';

input_option.type='dir';
input_option.ext='.mat';
pos_file_list=FileInput(file_name1,input_option);
length_data=length(pos_file_list.data);

%%
for k=1:length_data

    signalname=char(pos_file_list.data(1,k));
    load(signalname);
    train_input=EEGdata(:,1:5:end);
    EEGdata=train_input';
   
    s=[file_name2,num2str(k),'.mat'];
    save(s,'EEGdata');
    
end