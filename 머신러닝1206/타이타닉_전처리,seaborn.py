
## 필요 데이터 전처리 작업
# 1] 결측값 확인
# 2] Name필드 호칭정리 후 새로운 필드 title 추가 맨 끝에 
# 3] Name필드 삭제
# 4] Age필드는 엄청난 결측값= NaN 해결하기 ==>>  적절한 대치값을 찾음 ( mean[평균값], medien[중앙값] )

import pandas as pd
import numpy as np
import time
import seaborn as sns
import matplotlib   
import matplotlib.pyplot as plt   
from matplotlib  import font_manager
import matplotlib as mpl # 음수 표시 에러 

mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False
font_name = font_manager.FontProperties(fname='/Users/j.ena/Library/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시 


train = pd.read_csv('./titanic/train.csv')
test = pd.read_csv('./titanic/test.csv')

######## 1] 결측값 확인
print( 'train 누락값 갯수 확인 ', train.isnull().sum())
print()
print( 'test 누락값 갯수 확인 ', test.isnull().sum())

######## 2] 새로운 필드 title 만들고 분류하기
train_test_data = [train, test]

for dt in train_test_data:
    dt['Title'] = dt['Name'].str.extract('([a-zA-Z]+)\.', expand=False )

# 숫자로 분류시키기 (Title map) => Title 컬럼
# Mr : 0
# Miss : 1
# Mrs: 2
# Others: 3
title_mapping ={
    'Mr':0, 'Miss':1, 'Mrs':2, 
    'Master':3, 'Dr':3, 'Rev':3, 'Col':3, 'Major':3, 'Mlle':3,  'Countess':3, 
    'Ms':3, 'Lady':3, 'Jonkheer':3, 'Don':3, 'Dona':3, 'Mme':3, 'Capt':3, 'Sir':3
}
for dt in train_test_data:
    dt['Title'] = dt['Title'].map(title_mapping)

print(train.head(5))
print()
print(test.head(5))
print()

'''
#####################################    seaborn그래프    #############################################
def bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts()
    dead = train[train['Survived']==0][feature].value_counts()
    df = pd.DataFrame([survived,dead])
    df.index = ['Survived','Dead']
    df.plot(kind='bar',stacked=True, figsize=(10,5))
########################################################################################################
# bar_chart('Title')
# plt.title('남성:0  Miss:1 Mrs:2 나머지:3')
# plt.show()
'''

######## 순서3]  호칭정보 Title필드 처리했으니 Name필드삭제 가능 drop키워드 
train.drop('Name', axis=1, inplace=True)
test.drop('Name', axis=1, inplace=True)

print('+ ' * 70 )
print(train.head(5))
print()
print(test.head(5))
print()

######## 순서4]  Age필드는 엄청난 결측값=NaN 해결 ==> 적절한값대체고민 평균값 mean, 중앙값 median 
# fillna() groupby그룹필드, transform()
# train['Age'].fillna( group().tranform()~~,   inplace=True)
train['Age'].fillna( train.groupby('Title')['Age'].transform('median'),   inplace=True)
test['Age'].fillna( test.groupby('Title')['Age'].transform('median'),   inplace=True)
# ㄴㄴ 나이Age결측값 새로생성된 Title필드 median값 대체 fillna채워
# ㄴㄴ 16미만 0  17~26 1   27~36 2   37~66  3   67이상  4
 
for dt in train_test_data:
    dt.loc[ (dt['Age'] < 16), 'Age'] = 0
    dt.loc[ (dt['Age'] >= 16) & (dt['Age'] <= 26) , 'Age'] = 1
    dt.loc[ (dt['Age'] >= 27) & (dt['Age'] <= 36) , 'Age'] = 2
    dt.loc[ (dt['Age'] >= 37) & (dt['Age'] <= 66) , 'Age'] = 3
    dt.loc[ (dt['Age'] >= 67) , 'Age'] = 4

print(train.head(5))
print()
print(test.head(5))
print()

# bar_chart('Age')
# plt.title(' 16미만 0  17~26 1   27~36 2   37~66  3   67이상  4 ')
# plt.show()


'''
PassengerId: 탑승자 데이터 일련번호
Survived: 생존여부, 0 = 사망, 1 = 생존
Pclass: 티켓의 선실 등급, 1 = 일등석, 2 = 이등석, 3 = 삼등석
Sex: 탑승자 성별
Name: 탑승자 이름
Age: 탑승자 나이
SibSp: 같이 탑승한 형제, 자매 또는 배우자 인원 수
Parch: 같이 탑승한 부모님 또는 자녀 인원 수
Ticket: 티켓 번호
Fare: 요금
Cabin: 선실 번호
Embarked: 탑승 항구, C = Cherbourg, Q = Queenstown, S = Southampton
'''


print()
print()