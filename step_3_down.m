%% 
% �²�����200HZ�� 

%�����շ������ݣ�EEGdata;
%ͼƬ�շ������ݣ��ֱ���face(renlian),food(wucan),landscape(fengjing),
%...sick(exin),snake(she),spider(zhizhu)
%label:excited-4,happy-3,peace-2,sad-1,fear-0

%%
close all
clear all
clc

addpath('C:\EEG\eeg_function');

%���������
file_name1='C:\EEG\eeg_DATA\shmtulab_seed\LSMA_zhou';
%�²����任�����������
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