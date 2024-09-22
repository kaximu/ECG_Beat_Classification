import os
from tqdm import tqdm
import numpy as np
import random
#from utils import *



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

nums = ['100','101','102','103','104','105','106','107','108','109'
    ,'111','112','113','114','115','116','117','118','119','121'
    ,'122','123','124','200','201','202','203','205','207','208','209'
    '210','212','213','214','215','217','219','220','221','222','223'
    ,'228','230','231','232','233','234']

feature = ['MLII','V1','V2','V4','V5']

testset = ['101','105','114','118','124','201','210','217']
trainset = [x for x in nums if x not in testset]

