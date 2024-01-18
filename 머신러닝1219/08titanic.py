import pandas as pd
import numpy as np
import os
from tensorflow import keras
from copy import copy
import time


#그래프시각화
import seaborn as sns
import matplotlib   
import matplotlib.pyplot as plt   
from matplotlib  import font_manager
import matplotlib as mpl 
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)


def file_data(path):
    result = dict()
    for fn  in  os.listdir(path):
        file_name = fn[0:-4]
        result[file_name] = pd.read_csv(path+'/'+fn)
    return result

# 순서1] data폴더 파일이름추출 
path = './data'
data = file_data(path)
print( list(data.keys()) )
key = list(data.keys())
print(data[key[0]])  # [418 rows x 2 columns]   gender_submission
print(data[key[1]])  # [418 rows x 11 columns]  test
print(data[key[2]])  # [891 rows x 12 columns]  train
print()  

#판다스 머지merge, concat  gender_submission문서, test문서   
# 순서2] 데이터 merge
def make_merge(data) :
    test_dataSet = pd.merge(data['gender_submission'], data['test'], how='outer', on='PassengerId' )
    newData = pd.concat( [data['train'], test_dataSet] )
    newData.reset_index(drop=True, inplace=True)
    return newData

print()
time.sleep(1)
rawdata = make_merge(data)
print(rawdata) #[1309 rows x 12 columns]
# PassengerId  Survived  Pclass  Name  Sex   Age  SibSp  Parch   Ticket   Fare Cabin Embarked
'''
      PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch              Ticket      Fare Cabin Embarked
0               1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0           A/5 21171    7.2500   NaN        S
1               2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0            PC 17599   71.2833   C85        C
2               3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0    STON/O2. 3101282    7.9250   NaN        S
1306         1307         0       3                       Saether, Mr. Simon Sivertsen    male  38.5      0      0  SOTON/O.Q. 3101262    7.2500   NaN        S
1307         1308         1       3                                Ware, Mr. Frederick    male   NaN      0      0              359309    8.0500   NaN        S
1308         1309         1       3                           Peter, Master. Michael J    male   NaN      1      1                2668   22.3583   NaN        C

'''

print()
print('= ' * 70)
# 순서3] 데이터 rawdata구조에서 필드제거  Name필드 , Ticket필드 2개 필드  삭제 drop,remove,del[]
def remove_column(rd, remove_list):
    result = copy(rawdata)
    result.set_index("PassengerId", inplace = True) # PassengerId를 Index로 하자.

    for column in remove_list:
        del(result[column])
    return result

remove_list = ['Name', 'Ticket']
ret1 = remove_column(rawdata, remove_list)
print(ret1) #Name,Ticket필드 제거 
print('Name필드, Ticket필드삭제 성공')


# 순서4] 데이터 결측값 Age필드, Cabin필드
#결측값갯수
print('12-22금요일 결측값갯수 =', ret1.isnull().sum())
print()

def missing_value(ret):
    del(ret["Cabin"])
    ret.dropna(inplace = True)

missing_value(ret1)
print(ret1) #[1043 rows x 8 columns]  Cabin필드 삭제



# 순서5] 성별, Embarked처리
# Sex: male = 0, female = 1
# Embarked: C = 0, Q = 1, S = 2
# Embarked: 탑승 항구, C = Cherbourg세르부르 프랑스, Q = 아일랜드 Queenstown, S = Southampton
ret1["Sex"] = np.where(ret1["Sex"].to_numpy() == "male", 0, 1)
ret1["Embarked"] = np.where(ret1["Embarked"].to_numpy() == "C", 0, np.where(ret1["Embarked"].to_numpy() == "Q", 1, 2))
print(ret1)
print('Sex, Embarked 성공  ')
print()


# 순서6] Label  생성
y_test, y_train = ret1["Survived"][:300].to_numpy(), ret1["Survived"][300:].to_numpy()
del(ret1["Survived"])
X_test, X_train = ret1[:300].values, ret1[300:].values
print('X_train =' , X_train)
print()
print('y_test =' , y_test)
print()
print('["Survived"] 레이블 성공  ')


# 순서7] 딥러닝 모델생성
from tensorflow.keras import Model, layers 
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout, BatchNormalization

model = keras.Sequential()
model.add(BatchNormalization())
model.add( Dense(120, activation='relu' ))
model.add( Dropout(0.10)) #과적합 예방역할
model.add( Dense(64, activation='relu' ))
model.add( Dropout(0.10)) #과적합 예방역할
model.add( Dense(32, activation='relu' ))
model.add( Dropout(0.10)) #과적합 예방역할
model.add( Dense(16, activation='relu' ))
model.add( Dropout(0.70)) #과적합 예방역할
model.add( Dense(1, activation='softmax' ))

# 순서8] 딥러닝 모델최적화 SGD(), Adam() & 컴파일compile()
# 최적화 SGD, Adam( )
opt = keras.optimizers.Adam(0.01)
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['binary_accuracy'] )

# 순서9] 모델훈련 fit( 대상은 train꺼,  epochs)
np.random.seed(1234)
index_list = np.arange(0, len(y_train))
valid_index = np.random.choice(index_list, size = 200, replace = False)
valid_train =  X_train[valid_index]
valid_labels = y_train[valid_index]
history = model.fit(X_train, y_train, epochs=200,  validation_data=(valid_train, valid_labels) )
# history = model.fit(X_train, y_train, epochs=200 ,validation_data=(X_train, y_train) )
print('모델 fit 진행')
print()

print(' history.history데이터출력 ' ,history.history ) #다시확인
mydata = pd.DataFrame(history.history)
print(mydata)
mydata.to_csv('./data/mydata.csv')

plt.plot( history.history['loss'])  
plt.title('model fit')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()


# 순서10] 모델 predict예측을 위해서 test용
pred = model.predict(X_test).reshape(X_test.shape[0])
pred = np.where(pred>0.5, 1, 0)
guess  = 1 - ( np.where((pred-y_test) == 0,0,1).sum()/len(y_test)  )
print('정확도 : ', guess)


print()
print('- ' * 70)