close all
clear all
clc

x=[];
y=[];

load('C:\EEG\eeg_DATA\music\music_cnn\dSample.mat');
x=train_input;
y=train_output.*0;

load('C:\EEG\eeg_DATA\picutre_emotion\cnn_data\dSample.mat');
x=[x;train_input];
y=[y;train_output.*0+1];

load('C:\EEG\eeg_DATA\shmtulab_seed\cnn_Sample\dSample.mat');
x=[x;train_input];
y=[y;train_output.*0+2];

train_input=x;
train_output=y;
save('S3_Sample.mat','train_input','train_output');