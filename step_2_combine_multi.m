close all
clear all
clc

%输入的数据
x=[];
y=[];

load('C:\EEG\eeg_DATA\music\music_cnn\dSample.mat');
x=train_input;
y=train_output;

load('C:\EEG\eeg_DATA\picutre_emotion\cnn_data\dSample.mat');
x=[x;train_input];
y=[y;train_output+5];

load('C:\EEG\eeg_DATA\shmtulab_seed\cnn_Sample\dSample.mat');
x=[x;train_input];
y=[y;train_output+11];

train_input=x;
train_output=y;
save('emotion_bigSample.mat','train_input','train_output');