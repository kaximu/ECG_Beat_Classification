import os
from tqdm import tqdm
import numpy as np
import random
from utils import *
import wfdb
import matplotlib.pyplot as plt
from sklearn import preprocessing
from scipy.signal import find_peaks


# constant parameters
spilt = True
input_size = 256
use_network = False
filter_lenght = 32
kernel_size = 16
drop_rate = 0.2
feature = 'MLII'
epoch = 10
batch = 256
classes = ['N','V','/','A','F','~']
MIT_BIH_DIR = './Dataset/MIT-BIH'



record = wfdb.rdrecord('./Dataset/MIT-BIH/100')
signal0 = preprocessing.scale(np.nan_to_num(record.p_signal[:,0])).tolist()
signal1 = preprocessing.scale(np.nan_to_num(record.p_signal[:,1])).tolist()


peaks,_ = find_peaks(signal0,distance=150)

for peak in peaks[1:-1]:
    start = peak-input_size//2
    end = peak+input_size//2
    
    ann = wfdb.rdann('./Dataset/MIT-BIH/100', extension='atr',sampfrom=start
                     ,sampto=end)
    beat,dic = wfdb.rdsamp('./Dataset/MIT-BIH/100',sampfrom=start,sampto=end,
                       channels=[0])
    plt.subplot(10, 5,1)
    plt.plot(beat)
    annsymbol = ann.symbol
    print (annsymbol)
    

# List of record names to process
record_names = ['100','101','102','103','104','105','106','107','108','109'
    ,'111','112','113','114','115','116','117','118','119','121'
    ,'122','123','124','200','201','202','203','205','207','208','209'
    '210','212','213','214','215','217','219','220','221','222','223'
    ,'228','230','231','232','233','234']

feature = ['MLII','V1','V2','V4','V5']

testset = ['101','105','114','118','124','201','210','217']
trainset = [x for x in record_names if x not in testset]
#for record_name in record_names:
    # Read the record and annotations
    #record = wfdb.rdrecord(os.path.join(MIT_BIH_DIR, record_name))
    #annotation = wfdb.rdann(os.path.join(MIT_BIH_DIR, record_name), 'atr')
    #ecg_signal = record.p_signal[:, 0]  # Get the first channel
    #qrs_indices = annotation.sample  # QRS beat indices
    # Plot the ECG signal
    #plt.figure(figsize=(12, 6))
    #plt.plot(ecg_signal, label='ECG Signal')
    #plt.title(f'ECG Signal from Record {record_name}')
    #plt.xlabel('Samples')
    #plt.ylabel('Amplitude')
    #plt.legend()
    
    # Highlight the QRS beats on the plot
    #for index in qrs_indices:
        #plt.axvline(x=index, color='r', linestyle='--', label='QRS Beat' if index == qrs_indices[0] else "")
    
    #plt.show()
    #print(f"Number of QRS Beats detected in Record {record_name}: {len(qrs_indices)}")