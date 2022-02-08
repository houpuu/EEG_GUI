%% 
% 1，生成2s为长度的样本，滑窗的尺寸是0.3s；
% 2,下采样到200HZ，生成400长度为单位的样本； 

%音乐诱发的数据，EEGdata;
%图片诱发的数据，分别是face(renlian),food(wucan),landscape(fengjing),
%...sick(exin),snake(she),spider(zhizhu)
%label:excited-4,happy-3,peace-2,sad-1,fear-0

%%
close all
clear all
clc

addpath('C:\FangCloudV2\personal_space\eeg_program\function');
addpath('C:\EEG\eeg_function');

%输入的数据
file_name1='C:\EEG\eeg_DATA\music\music_LSMA\fear';
%下采样变换后的样本保存
file_name2='C:\EEG\eeg_DATA\music\music_sample\fear_';

input_option.type='dir';
input_option.ext='.mat';
pos_file_list=FileInput(file_name1,input_option);
length_data=length(pos_file_list.data);

%%
for k=1:length_data

    S_signalname=char(pos_file_list.data(1,k));
    load(S_signalname);
    train_input=sliding_window(EEGdata,2000,400,5);
   
    s=[file_name2,num2str(k),'.mat'];
    save(s,'train_input','train_output');
    
end