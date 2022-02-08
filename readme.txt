step1_main_LSMA.m 
对数据进行滤波；数据输出EEGdata。
输入：格式：16*length，输出：格式：16*length。

step2_sample.m（用于cnn的训练和测试）
1，首先对单个情绪的数据进行处理，滑窗取样（sliding_window.m）同时进行了下采样，
     得到N*400*16的train_input，标签train_output，
2，然后把所有的数据放在一个文件里，对所有数据形成一个所有样本的数据集.
输入：16*length，输出：N*400*16.

step3_down.m + DownSample.m （只用来做测试）
对数据直接进行下采样，主要是针对测试数据，不需要制作样本的数据。
输入EEGdata，格式16*length， 输出：(length/5)*16