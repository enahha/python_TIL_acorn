import time
import pandas as pd
from sklearn.datasets import fetch_openml

import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
import warnings

font_name = font_manager.FontProperties(fname='/Users/j.ena/Library/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False   # 음수값 표식여부 
warnings.filterwarnings('ignore')

'''
 	종류	설명
1	StandardScaler	기본 스케일. 평균과 표준편차 사용
2	MinMaxScaler	최대/최소값이 각각 1, 0이 되도록 스케일링
3	MaxAbsScaler	최대절대값과 0이 각각 1, 0이 되도록 스케일링
4	RobustScaler	중앙값(median)과 IQR(interquartile range) 사용. 아웃라이어의 영향을 최소화
'''

# scaler : 최적화 과정에서의 안정성 및 수렴 속도를 향상
np.random.seed(1234) #난수발생 균일화 
matrix = np.random.randint(-1000, 1000, 20).reshape(10,2)
data = pd.DataFrame(matrix)
print(data)

#첫번째표준 StandardScaler
from sklearn.preprocessing import StandardScaler
StandardScaler = StandardScaler()
StandardScaler.fit(matrix)
matrix = StandardScaler.transform(matrix)
print()
print('1번째 표준 StandardScaler')
print(matrix)

#2번째 MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
MinMaxScaler = MinMaxScaler()
MinMaxScaler.fit(data)
print()
print('2번째 MinMaxScaler ')
data = MinMaxScaler.transform(data)
df=pd.DataFrame(data)
print(df)

#3번째  MaxAbsScaler
from sklearn.preprocessing import MaxAbsScaler
MaxAbsScaler = MaxAbsScaler()
MaxAbsScaler.fit(data)
print()
print('3번째 MaxAbsScaler ')
data = MaxAbsScaler.transform(data)
df = pd.DataFrame(data)
print(df)

#4번째 RobustScaler
from sklearn.preprocessing import RobustScaler
RobustScaler = RobustScaler()
RobustScaler.fit(data)
print()
print('4번째 RobustScaler ')
data = RobustScaler.transform(data)
df = pd.DataFrame(data)
print(df)


print()
print()
