% 1�������ݽ���LSMA��Ԥ�˲�
% 2,�²�����200HZ������400����Ϊ��λ�������� 

%�����շ������ݣ�EEGdata;
%ͼƬ�շ������ݣ��ֱ���face(renlian),food(wucan),landscape(fengjing),
%...sick(exin),snake(she),spider(zhizhu)
%label:excited-4,happy-3,peace-2,sad-1,terrifying-0

close all
clear all
clc

addpath('C:\FangCloudV2\personal_space\eeg_program\function');
addpath('C:\EEG\eeg_function');
%���������
file_name2='C:\EEG\eeg_DATA\music\music_LSMA\sad_sub99_';
%LSMA�˲�������ݱ���
file_name1='C:\EEG\eeg_DATA\music\music_LSMA\sad\sub99';
%�²����任������ݱ���

input_option.type='dir';
input_option.ext='.mat';
pos_file_list=FileInput(file_name1,input_option);
length_data=length(pos_file_list.data);

for k=1:length_data
    %1--LSMA-------------
    S_signalname=char(pos_file_list.data(1,k));
    load(S_signalname);
    s=[file_name2,num2str(k),'.mat'];
    save(s,'EEGdata');
end


