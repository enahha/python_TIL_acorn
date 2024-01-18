# null 값이 없게 데이터 전처리를 해주어야 한다 ==>
# 훈련데이터와 테스트데이터의 차이 = null값을 없애준다, 너무 긴 Name값을 encoding시켜준다

## 필요 데이터 전처리 작업
# 1] 결측값 확인
# 2] Name필드 호칭정리 후 새로운 필드 title 추가 맨 끝에 나중에 Name필드 삭제

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


#sns이용한 그래프
# import matplotlib.pyplot as plt
# import seaborn as sns
# def bar_chart(feature):
#     survived = train[train['Survived']==1][feature].value_counts()
#     dead = train[train['Survived']==0][feature].value_counts()
#     df = pd.DataFrame([survived,dead])
#     df.index = ['Survived','Dead']
#     df.plot(kind='bar',stacked=True, figsize=(10,5))
    

# print('train[Pclass].unique() ', train['Pclass'].unique())
# bar_chart('Pclass')
# plt.title('Pclass ok')
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


'''

print()
print()