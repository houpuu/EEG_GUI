step1_main_LSMA.m 
1, 对数据进行滤波；数据输出EEGdata。
输入：格式：16*length，输出：格式：16*length。

step2_sample_1.m（用于cnn的训练和测试）
2, 首先对单个情绪的数据进行处理，滑窗取样（sliding_window.m）同时进行了下采样，
     得到N*400*16的train_input，标签train_output，

step_2_combine.m 
3, 然后把所有的数据放在一个文件里，对所有数据形成一个所有样本的数据集.
输入：16*length，输出：N*400*16.

step3_down.m + DownSample.m （只用来做测试）
4, 对数据直接进行下采样，主要是针对测试数据，不需要制作样本的数据。
输入EEGdata，格式16*length， 输出：(length/5)*16

step4_relabel.m 
5, 重新对数据贴标签（输入和输出格式一样）
N*400*16的train_input，标签train_output，