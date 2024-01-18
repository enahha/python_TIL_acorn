
import time
import numpy as np
import pandas as pd
#sk머신러닝 라이브러리 공색  from  sklearn. ~~ import 함수이름
from sklearn.svm import SVC, SVR

import seaborn as sns 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

df = pd.read_csv('./data/iris.csv')
print(df)
print(df.info())
# print(df.describe())
print()


data = df[ ['SepalLength', 'SepalWidth', 'PetalLength' ,'PetalWidth'] ]
print(data.columns)

label = df['Name']
#sklearn학습이론적용을위해서 데이터 분리 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.3, train_size=0.7, shuffle=True)
# [150 rows x 5 columns]
print(x_train.shape, x_test.shape) #(105, 4) (45, 4)
print()
print(y_train.shape, y_test.shape) #(105,) (45,)
print('x_train.head() 훈련데이터 ' , x_train.head())
print('x_test.head() 테스트데이터 ' , x_test.head())
print()

# 실전훈련을 위해서 이미 생성된 훈련알고리즘 
# KNN, SVC, RamdomForest, DecisionTreeClass~
from sklearn.svm import SVC, SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 
#  svc =  support vector  classification 
#  svr =  support vector  regression회귀 

# KNeighborsClassifier()알고리즘
clf = KNeighborsClassifier() #학습함수지정
print('iris데이터 KNeighborsClassifier() 훈련중...')

# clf = SVC() #학습함수지정
# print('iris데이터 SVC() 훈련중...')

# clf = RandomForestClassifier() #학습함수지정
# print('iris데이터 RandomForestClassifier() 훈련중...')

# clf = DecisionTreeClassifier() #학습함수지정
# print('iris데이터 DecisionTreeClassifier() 훈련중...')

# clf = GaussianNB() #학습함수지정
# print('iris데이터 GaussianNB() 훈련중...')



clf.fit(x_train, y_train) ##(105, 4)
y_pred  = clf.predict(x_test)
print('ㄴy_pred ', y_pred)

time.sleep(1)
clf.predict([[6.7, 3.3, 5.7, 2.1]]) 
print('ㄴ정답률 =', accuracy_score(y_test, y_pred))
print(f'ㄴ정답률 = {round(accuracy_score(y_test, y_pred),2)*100}%')
#1 정답률 = 0.9555555555555556
#1 정답률 = 96.0%

#2 ㄴ정답률 = 0.9555555555555556
#2 ㄴ정답률 = 96.0%

# RandomForestClassifier()학습
#3 ㄴ정답률 = 0.9333333333333333
#3 ㄴ정답률 = 93.0%

# DecisionTreeClassifier()학습
# ㄴ정답률 = 0.9111111111111111
# ㄴ정답률 = 91.0%

#  GaussianNB()학습
# ㄴ정답률 = 0.9111111111111111
# ㄴ정답률 = 91.0%

print()
print('- ' * 70)
# 머신러닝, 딥러닝  
# 1번째 데이터수집
# 2번째 다양한 - 훈련알고리즘,  fit()훈련
# 3번째 정확도 
