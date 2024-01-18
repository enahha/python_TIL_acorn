import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from matplotlib import rc
from matplotlib import font_manager
font_name = font_manager.FontProperties(fname='/Users/j.ena/Library/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

df = pd.read_csv('./data/iris.csv')
print(df.info())
print(df.describe())

data = df[ ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'] ]
print(data.columns)

# Name 칼럼으로 종류 나누기
print(df['Name'].unique())

# # seaborn으로 데이터들의 분포를 그래프로 나타내기
# import seaborn as sns
# sns.pairplot(df, hue='Name', palette='husl')
# plt.show()

# ===============# ===============# ===============# ===============# ===============

# sklearn학습이론 적용을 위해서 데이터 분리하기
label = df['Name']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.3, train_size=0.7, shuffle=True) 
                                                    # 데이터를 test데이터와 train데이터를 7:3으로 분리
print('x_train shape>>>', x_train.shape, '\n', 'x_test shape>>>', x_test.shape)
print('y_train shape>>>', y_train.shape, '\n', 'y_test shape>>>', y_test.shape)
print('x_train.head() 훈련데이터 ', x_train.head())
print('x_test.head() 훈련데이터 ', x_test.head())

# ===============# ===============# ===============# ===============# ===============

# 실전훈련을 위해 이미 생성된 훈련알고리즘 ==> KNN, SVC, RandomForest, DecisionTreeClass~ 등의 모듈을 사용

## 예측하기 교제(파이썬 라이브러리를 활용한 머신러닝) 48페이지~
from sklearn.svm import SVC,SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier     # 결정
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score  # 정답 예측
# svc = support vector classification 예) 비온다, 안온다
# svr = support vector regression   회귀 57%

clf = KNeighborsClassifier()        # 학습함수지정
print('irise데이터 KNeighborsClassifier() 훈련중.....')
clf.fit(x_train,y_train) ## (105, 4)
# 예측 pred
y_pred = clf.predict(x_test)
print('붓꽃 예측 pred ' , y_pred)

time.sleep(1)
print(clf.predict( [ [6.7, 3.3, 5.7, 2.1] ] ) )  # 임의적으로 예측할 데이터

#------------------------------------------
# 예측 정확도를 나타내줌
print('정답률 = ', accuracy_score(y_test,y_pred))
print(f"정답률 = ", round(accuracy_score(y_test,y_pred),2)*100)
