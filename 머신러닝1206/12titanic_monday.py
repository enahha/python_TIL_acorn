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
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시 


train = pd.read_csv('./titanic/train.csv')
test = pd.read_csv('./titanic/test.csv')
print(train.tail(10))
print()
print(test.tail(10))
print()


#순서1] 결측값확인  train.isnull().sum() / test.isnull().sum()
print( '111111 train 누락값 갯수 확인 ', train.isnull().sum())
print()
print( '111111 test 누락값 갯수 확인 ', test.isnull().sum())

#순서2]  Name필드 호칭정리후 새로운 필드 Title추가 맨끝에 나중에 Name필드 삭제  
train_test_data  = [train, test]
for dt in train_test_data:
    dt['Title'] = dt['Name'].str.extract('([a-zA-z]+)\.', expand=False)

# 호칭데이터를 좀더 빠르게 머신학습처리를 위해서 숫자화 0Mr 1Miss 2Mrs 3기타
# 숫자로 분류시키기 (Title map) => Title 컬럼
# Mr : 0
# Miss : 1
# Mrs: 2
# Others: 3
title_mapping = {
    'Mr':0, 'Miss':1, 'Mrs':2, 
    'Master':3, 'Dr':3, 'Rev':3, 'Col':3, 'Major':3, 'Mlle':3,  'Countess':3, 
    'Ms':3, 'Lady':3, 'Jonkheer':3, 'Don':3, 'Dona':3, 'Mme':3, 'Capt':3, 'Sir':3
}

for dt in train_test_data:
    dt['Title']= dt['Title'].map(title_mapping)

print(train[20:31])
print()
print(test[20:31])
print()

########################################################################################################
def bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts()
    dead = train[train['Survived']==0][feature].value_counts()
    df = pd.DataFrame([survived,dead])
    df.index = ['Survived','Dead']
    df.plot(kind='bar',stacked=True, figsize=(10,5))
########################################################################################################
# bar_chart('Title')
# plt.title('남성:0  Miss:1 Mrs:2 나머지:3')
# plt.show()  주석처리 


#순서3]  호칭정보 Title필드 처리했으니 Name필드삭제 가능 drop키워드 
train.drop('Name', axis=1, inplace=True)  #axis=0생략하면 가로행, 특정열 Name열  
test.drop('Name', axis=1, inplace=True)   #inplace=True원본의 데이터 유지..
print(train[20:31])
print()
print(test[20:31])
print()


#순서4]  Age필드는 엄청난 결측값=NaN 해결 ==> 적절한값대체고민 평균값 mean, 중앙값 median 
# 나이필드 연령대 적절하게 구분  영유아, 아동=어린이, 청소년/청년   중장년  노년=시니어
# 나이필드 널값=결측일때 적절한 데이터값 대입 
# 훈련train 나이결측누락 177개   테스트test 나이결측누락 86개
#해결1 나이결측 첫번째 fillna(),groupby(),transform() 
#해결2 나이조건  5세미만0  6~14 1  15~25 2  26~36 3  37~50 4   51~65 5  66~ 6
train['Age'].fillna( train.groupby('Title')['Age'].transform('median'), inplace=True)
test['Age'].fillna( test.groupby('Title')['Age'].transform('median'), inplace=True)
print('train[Age]필드접근 ')
for dt in train_test_data:
    dt.loc[ (dt['Age'] <= 5) , 'Age'] = 0
    dt.loc[ (dt['Age'] >= 6) &  (dt['Age'] < 15)  , 'Age'] = 1
    dt.loc[ (dt['Age'] >= 15) &  (dt['Age'] < 26)  , 'Age'] = 2
    dt.loc[ (dt['Age'] >= 26) &  (dt['Age'] < 37)  , 'Age'] = 3
    dt.loc[ (dt['Age'] >= 37) &  (dt['Age'] < 51)  , 'Age'] = 4
    dt.loc[ (dt['Age'] >= 51) &  (dt['Age'] < 66)  , 'Age'] = 5
    dt.loc[ (dt['Age'] >= 66) , 'Age'] = 6

print(train[20:31])
print()
print(test[20:31])
print()

# bar_chart('Age')
# plt.title(' 5세미만0  6~14 1  15~25 2  26~36 3  37~50 4   51~65 5  66~ 6 ')
# plt.show()  나이연령대  생존 그래프  26~36 3


# 순서5] Embarked: 승선
# Embarked: 탑승 항구, C = Cherbourg, Q = Queenstown, S = Southampton
for dt in train_test_data:
    dt['Embarked'] = dt['Embarked'].fillna('S')

embarked_mapping = { 'S':0 , 'Q':1, 'C':2}
for dt in train_test_data:
    dt['Embarked'] = dt['Embarked'].map(embarked_mapping)
    
print(train[20:31])
print()
print(test[20:31])
print()

# bar_chart('Embarked')
# plt.title(' S = Southampton :0  Q = Queenstown 1  C = Cherbourg 2 ')
# plt.show() 출발항구  Southampton탑승한 사람 생존/사망

#순서6] Fare요금금액  
train['Fare'].fillna( train.groupby('Pclass')['Fare'].transform('median'), inplace=True)
test['Fare'].fillna( test.groupby('Pclass')['Fare'].transform('median'), inplace=True)
print('train[Fare]필드접근 ')
for dt in train_test_data:
    dt.loc[ (dt['Fare'] <= 10) , 'Fare'] = 0
    dt.loc[ ((dt['Fare'] > 10) &  (dt['Fare'] <= 50))  , 'Fare'] = 1
    dt.loc[ ((dt['Fare'] > 50) &  (dt['Fare'] <= 100))  , 'Fare'] = 2
    dt.loc[ (dt['Fare']  > 100) , 'Fare'] = 3

# bar_chart('Fare')
# plt.title('금액별 0~10 0  11~50 1  51~100 2   100이상 3')
# plt.show()


#순서7]Cabin 선실번호  승객승선한 고객들의 방=선실번호 캐빈는  Pclass필드연결 
# Pclass 1 = 일등석,  2 = 이등석,  3 = 삼등석
# Pclass 1   Pclass 2    Pclass 3   연결  Cabin필드 .str[0:1]

for dt in train_test_data:
    dt['Cabin'] = dt['Cabin'].str[:1]
    print('dt[Cabin] 첫글자출력 ', dt['Cabin'])

Pclass1 = train[train['Pclass']==1]['Cabin'].value_counts()
Pclass2 = train[train['Pclass']==2]['Cabin'].value_counts()
Pclass3 = train[train['Pclass']==3]['Cabin'].value_counts()
print('12-12-화요일 Pclass1 = ',Pclass1, ' Pclass2 =  ', Pclass2, '  Pclass3 = ',Pclass3 )
print('+ ' * 70)
#Pclass1는 ABCDET존재(F,G없음)  Pclass2는 ABCTG없음(D E F있음)   Pclass3는ABCDT없음(EFG있음) 

#상단에서 기술한 결측값확인  train.isnull().sum() / test.isnull().sum()
print( '77777 train 누락값 갯수 확인 ', train.isnull().sum())
print()
print( '77777 test 누락값 갯수 확인 ', test.isnull().sum())
print('+ ' * 70)


#12-12-화요일 Cabin열필드, Pclass열필드 상관관계, Cabin필드 결측값 null처리 설명
#Pclass1는 ABCDET존재(F,G없음)  Pclass2는 ABCTG없음(D E F있음)   Pclass3는ABCDT없음(EFG있음) 
cabin_mapping = { 'A':0 , 'B':1, 'C':2, 'D':3, 'C':4, 'E':5, 'F':6, 'G':7, 'T':8 }
for dt in train_test_data:
    dt['Cabin'] = dt['Cabin'].map(cabin_mapping)

train['Cabin'].fillna( train.groupby('Pclass')['Cabin'].transform('median'), inplace=True)
test['Cabin'].fillna( test.groupby('Pclass')['Cabin'].transform('median'), inplace=True)
print('Cabin필드=객실번호 fillna함수 test test 12-12-화요일 11시 ')
#전처리 
#train&test훈련적용 알고리즘 특징 파악 

# 가족수 FamilySize필드 = Parch + SibSp 
train['FamilySize'] = train['SibSp'] + train['Parch'] + 1
test['FamilySize'] = test['SibSp'] + test['Parch'] + 1

# Feature scaling 으로 매
family_mapping = { 1: 0, 2: 0.4, 3: 0.8, 4: 1.2, 5: 1.6, 
                  6: 2, 7: 2.4, 8: 2.8, 9: 3.2, 10: 3.6, 11: 4 }
for dt in train_test_data:
    dt['FamilySize'] = dt['FamilySize'].map(family_mapping)

print(train.head())
print()
print(test.head())
print()

#null대체 = 결측값해결 
#학습알고리즘 적용
# KNN, SVC, RamdomForest, DecisionTreeClass~
from sklearn.svm import SVC, SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 
#  svc =  support vector  classification 
#  svr =  support vector  regression회귀 

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# train_test_data  = [train, test]   이미 사용활용
dropped_data = [ 'Survived' , 'PassengerId' ]
train_data  =  train.drop(dropped_data, axis=1)
print()
print('train_data.isnull().sum() 합계확인 12-12-화요일 11:30  ')
print( train_data.isnull().sum())
print()
print( train_data.info())
print()

object_cols = train_data.select_dtypes(include=['object']).columns
train_data = train_data.drop(columns=object_cols)
k_fold =KFold(n_splits=10, shuffle=True, random_state=0)

clf = KNeighborsClassifier(n_neighbors=10) 
target = train['Survived']
score = cross_val_score(clf, train_data, target,
                          cv=k_fold,n_jobs=1, scoring='accuracy') #훈련데이터에서 분리한 검증한 점수 

print('결과 score ', score)
print('결과 score ', round(np.mean(score*100),2)) # 79.58%

# 타이타닉 주인공  디카프리오/윈슬릿/선장/주방조리사  생존할확률 
# 02sk_iris.py문서 비교 

from sklearn.preprocessing import LabelEncoder 
labelencoder = LabelEncoder()
labelencoder.fit(train['Sex'])
train['Gender'] = labelencoder.transform(train['Sex'])
print()
print(train.info())
print(train.head())
print()
train = train[ train['Fare'].notnull() ]  #결측값 제외시키는 방법 
print(train.head())

# 탐색적 데이터 분석 = EDA = exploratory Data Analysis 의  데이터최적화=전처리
# 전처리과정  결측값, 새로운필드,  계산연산을 위한  LabelEncoder 

# 맨끝에 필드 title필드추가
# titanic['title'] = titanic['title'].replace('Mlle', 'Miss')
# titanic['title'] = titanic['title'].replace('Ms', 'Miss')
# titanic['title'] = titanic['title'].replace('Mme', 'Mrs')
# Rare_f = ['Dona', 'Dr', 'Lady', 'the Countess']
# Rare_m = ['Capt', 'Col', 'Don', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Master']


# 훈련fit전에  validation훈련검증  k-fold  4개훈련후 1개 검증 
# 훈련알고리즘생성후  fit()훈련후 
# 예상 y_pred  = clf.predict(x_test)
# 예상 clf.predict([[6.7, 3.3, 5.7, 2.1]]) 
# 정답 accuracy_score(y_test, y_pred))

'''
train 훈련 데이터 확인 
     PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0              1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1              2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2              3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3              4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4              5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
..           ...       ...     ...                                                ...     ...   ...    ...    ...               ...      ...   ...      ...
886          887         0       2                              Montvila, Rev. Juozas    male  27.0      0      0            211536  13.0000   NaN        S
887          888         1       1                       Graham, Miss. Margaret Edith  female  19.0      0      0            112053  30.0000   B42        S
888          889         0       3           Johnston, Miss. Catherine Helen "Carrie"  female   NaN      1      2        W./C. 6607  23.4500   NaN        S
889          890         1       1                              Behr, Mr. Karl Howell    male  26.0      0      0            111369  30.0000  C148        C
890          891         0       3                                Dooley, Mr. Patrick    male  32.0      0      0            370376   7.7500   NaN        Q

[891 rows x 12 columns]

 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
test 테스트 데이터 확인
     PassengerId  Pclass                                          Name     Sex   Age  SibSp  Parch              Ticket      Fare Cabin Embarked
0            892       3                              Kelly, Mr. James    male  34.5      0      0              330911    7.8292   NaN        Q
1            893       3              Wilkes, Mrs. James (Ellen Needs)  female  47.0      1      0              363272    7.0000   NaN        S
2            894       2                     Myles, Mr. Thomas Francis    male  62.0      0      0              240276    9.6875   NaN        Q
3            895       3                              Wirz, Mr. Albert    male  27.0      0      0              315154    8.6625   NaN        S
4            896       3  Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female  22.0      1      1             3101298   12.2875   NaN        S
..           ...     ...                                           ...     ...   ...    ...    ...                 ...       ...   ...      ...
413         1305       3                            Spector, Mr. Woolf    male   NaN      0      0           A.5. 3236    8.0500   NaN        S
414         1306       1                  Oliva y Ocana, Dona. Fermina  female  39.0      0      0            PC 17758  108.9000  C105        C
415         1307       3                  Saether, Mr. Simon Sivertsen    male  38.5      0      0  SOTON/O.Q. 3101262    7.2500   NaN        S
416         1308       3                           Ware, Mr. Frederick    male   NaN      0      0              359309    8.0500   NaN        S
417         1309       3                      Peter, Master. Michael J    male   NaN      1      1                2668   22.3583   NaN        C


train 누락값 갯수 확인  PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

test 누락값 갯수 확인  PassengerId      0
Pclass           0
Name             0
Sex              0
Age             86
SibSp            0
Parch            0
Ticket           0
Fare             1
Cabin          327
Embarked         
'''



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

'''
print('train 훈련 데이터 확인 ')
print(train)
print()
print(' -' * 50)
print('test 테스트 데이터 확인 ')
print(test)
print()
print(' -' * 50)


print( 'train 누락값 갯수 확인 ', train.isnull().sum())
print()
print( 'test 누락값 갯수 확인 ', test.isnull().sum())

train 누락값 갯수 확인  PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

test 누락값 갯수 확인  PassengerId      0
Pclass           0
Name             0
Sex              0
Age             86
SibSp            0
Parch            0
Ticket           0
Fare             1
Cabin          327
Embarked         0
dtype: int64
'''

print()
print()