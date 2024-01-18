import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml


housing = fetch_openml(name="house_prices", as_frame=True)

# X
X = housing['data']
feature_names = housing['feature_names']

# Y
Y = housing['target']

df = pd.DataFrame(X, columns = feature_names)
print(df)
print('-' * 80)

df0 = df.select_dtypes(include=['float','int'])
df1 = df0.drop(['Id'], axis=1)
df2 = df1.dropna(axis=1)
df2.hist(bins=20, figsize=(5,10))
plt.show()

# 행들이 많아 데이터 정리하기
drop_col = ['LotArea','BsmtFinSF2','LowQualFinSF','2ndFlrSF','BsmtHalfBath','KitchenAbvGr','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal']
df3 = df2.drop(drop_col, axis=1)
df3.hist(bins=30, figsize=(14,8))
plt.show()

# 머신러닝 sklear사용 ========================================
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df3, Y, random_state=777)
print('X_train.shape, X_test.shape ' , X_train.shape, X_test.shape)
print('y_train.shape, y_test.shape ' , y_train.shape, y_test.shape)

print('y_train.mean() ' , y_train.mean(),'\t y_train.std()',y_train.std())
print('y_test.mean() ' , y_test.mean(),'\t y_test.std()',y_test.std())
print()

print('df3.mean() ' , df3.mean() )

'''
Fireplaces의 평균은 0.6인데 YrSold의 평균은 2007입니다. 하나는 면적이고 하나는 년도이니 단위(scale)가 다른건 당연합니다.
문제는 scale이 매우 다를 경우, Y를 예측하는데 미치는 영향 정도가 달라지게 된다는 점입니다.
보다 원활한 학습의 진행을 위해서는 정규화를 진행할 필요가 있습니다.
분야에 따라 서로 각기다른 정규화를 사용하기도 하고, 새로운 방식을 만들어내기도 합니다.
sklearn.preprocessing에서 제공하는 대표적인 정규화 scaler는 다음과 같습니다.

StandardScaler : (평균=0, 분산=1)이 되도록 조정합니다.
MinMaxScaler : 모든 값이 0~1 사이에 오도록(최대값=1, 최소값=0) 조정합니다.
RobustScaler : 최대, 최솟값 대신 사분위값(Q1, Q2, Q3)를 사용해 조정합니다.
'''


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

scaler.fit(X_train)
X_scaled_train = scaler.transform(X_train)
X_scaled_test = scaler.transform(X_test)

data = pd.DataFrame(X_scaled_train)
print(data.describe())
print()
time.sleep(1)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_scaled_train, y_train)

pred_train = model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)
print('12-07-목요일  훈련train 측정score ' ,model.score(X_scaled_train, y_train))
# 12-07-목요일  훈련train 측정score  0.7842596317643711
pred_test = model.predict(X_scaled_test)
print('12-07-목요일 테스트test 측정score ' ,model.score(X_scaled_test, y_test) )
# 12-07-목요일 테스트test 측정score  0.8739612215908215

# 회귀모델에서 가장 많이 사용되는 평가지표 중 하나는 RMSE(Root Mean Squared Error)입니다.
# 평가지표 MSE(Mean Squared Error), RMSE, MAE(Mean Absolute Error), R2(R-Squard)
import numpy as np
from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y_test,pred_test)
print('평가지표 평균오차 ' , np.sqrt(MSE)) # 평균적인 오차가 대략 24,500 달러
print('테스트test 평균  ', y_test.mean()) # 평균 약 175,000 달러


print()
print()
