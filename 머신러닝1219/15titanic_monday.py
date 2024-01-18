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


titanic_df = pd.read_csv('./data/train.csv')

print(titanic_df.tail(10))
print()
print(titanic_df.info())
print()

#순서1] 결측값확인  train.isnull().sum() / test.isnull().sum()
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace = True) # Age의 평균값으로 결측치 대체
titanic_df['Cabin'].fillna('N', inplace = True) # 'N'으로 대체
titanic_df['Embarked'].fillna('N', inplace = True) # 'N'값으로 대체
print(titanic_df.info())
print()

print('Sex 값 분포 : \n', titanic_df['Sex'].value_counts())
print('\n')
print('Cabin 값 분포 : \n', titanic_df['Cabin'].value_counts())
print('\n')
print('Embarked 값 분포 : \n', titanic_df['Embarked'].value_counts())

print()
titanic_df['Cabin'] = titanic_df['Cabin'].str[:1] # str은 글자를 추출하기위한 메소드
print(titanic_df['Cabin'].head())


# 성별에 따른 생존자 수 확인하기
print()
print(titanic_df.groupby(['Sex', 'Survived'])['Survived'].count())
# sns.barplot(x = 'Sex', y = 'Survived', data = titanic_df)
# plt.show()

# sns.barplot(x = 'Pclass', y = 'Survived', hue = 'Sex', data = titanic_df)
# plt.show()
print()


def get_category(age) :
    cat = ''
    if age <= -1 : cat = 'Unknown'
    elif age <= 5 : cat = 'Baby'
    elif age <= 12 : cat = 'Child'
    elif age <= 18 : cat = 'Teenager'
    elif age <= 25 : cat = 'Student'
    elif age <= 50 : cat = 'Young Adult'
    elif age <= 65 : cat = 'Adult'
    else : cat = 'Elderly'
    
    return cat


plt.figure(figsize = (10, 6))
# X축의 값을 순차적으로 표시하기 위한 설정
group_names = ['UnKnown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Elderly']

# lambda 식에 위에서 생성한 get_category()함수를 반환값으로 지정
# get_category(X)는 입력값으로 'Age'칼럼 값을 받아서 해당하는 cat 반환
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
sns.barplot(x = 'Age_cat', y = 'Survived', hue = 'Sex', data = titanic_df, order = group_names)
plt.show()
titanic_df.drop('Age_cat', axis = 1, inplace = True)
print()
#  Sex, Age, PClass 등이 생존을 좌우하는 중요한 피처인 것을 확인
# ML 알고리즘 모델적용


from sklearn import preprocessing

#여러 칼컴을 레이블 인코딩 하기
def encode_features(dataDF) :
    features = ['Cabin', 'Sex', 'Embarked']
    for feature in features :
        le = preprocessing.LabelEncoder()
        le.fit(dataDF[feature])
        dataDF[feature] = le.transform(dataDF[feature])
    return dataDF

print('+ ' * 80)
titanic_df = encode_features(titanic_df)
print(titanic_df.head())
print()


# Null 처리 함수
def fillna(df) : 
    df['Age'].fillna(df['Age'].mean(), inplace = True)
    df['Cabin'].fillna('N', inplace = True)
    df['Embarked'].fillna('N', inplace = True)
    df['Fare'].fillna(0, inplace = True)
    return df

# 머신러닝 알고리즘에 불필요한 속성 제거
def drop_features(df) :
    df.drop(['PassengerId', 'Name', 'Ticket'], axis = 1, inplace = True) # 모두 단순 구분을 위한 컬럼들
    return df

# 레이블 인코딩 수행
def format_features(df) :
    df['Cabin'] = df['Cabin'].str[:1]
    features = ['Cabin', 'Sex', 'Embarked']
    for feature in features :
        le = preprocessing.LabelEncoder()
        le.fit(df[feature])
        df[feature] = le.transform(df[feature])
    return df


# 함수를 모두 통함
def transform_features(df) :
    df = fillna(df)
    df = drop_features(df)
    df = format_features(df)
    return df


# 데이터를 재로딩하고, 피처 데이터 세트와 레이블 데이터 세트 추출
titanic_df = pd.read_csv('data/train.csv')
y_titanic_df = titanic_df['Survived']
X_titanic_df = titanic_df.drop('Survived', axis = 1, inplace = False)
X_titanic_df = transform_features(X_titanic_df)

#  train_test_split( )이용해 train데이터80 /test데이터20  세트를 추출하겠습니다
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_titanic_df, y_titanic_df, test_size = 0.2, random_state = 11)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 각 모델에 대한 Classifier 클래스 생성
dt_clf = DecisionTreeClassifier(random_state = 11)
rf_clf = RandomForestClassifier(random_state = 11)
lr_clf = LogisticRegression(random_state = 11)

# DecisionTreeClassfier 학습/예측평가
dt_clf.fit(X_train, y_train)
dt_pred = dt_clf.predict(X_test)
print('DecisionTreeClassifier 정확도 : {0:.4f}'.format(accuracy_score(y_test, dt_pred)))

# RandomForestClassifier 학습/예측/평가
rf_clf.fit(X_train, y_train)
rf_pred = rf_clf.predict(X_test)
print('RandomForestClassifier 정확도 : {0:.4f}'.format(accuracy_score(y_test, rf_pred)))

# LogisticRegression 학습/예측/평가
lr_clf.fit(X_train, y_train)
lr_pred = lr_clf.predict(X_test)
print('로직LogisticRegression 정확도 : {0:.4f}'.format(accuracy_score(y_test, lr_pred)))
print()
# DecisionTreeClassifier 정확도 : 0.7877
# RandomForestClassifier 정확도 : 0.8547
# 로직LogisticRegression 정확도 : 0.8492


# 3개의 알고리즘 중 LogisticRegression이 타 알고리즘에 비해 높은 정확도를 나타내고 있습니다. 
# 아직 최적화 작업을 수행하지 않았고, 데이터 양도 충분하지 않기에 LogistiocRegression이 가장 좋은 모델이라고 할 수는 없습니다. 
# 교차 검증으로 결정 트리 모델을 좀 더 평가
# model_selection 패키지의 KFold, cross_val_score( ), GridSearchCV 클래스를 모두 사용

from sklearn.model_selection import KFold
def exec_kfold(clf, folds = 5) :
    # 폴드 세트가 5개인 KFold 객체 생성. 폴드 수만큼 예측결과 저장 위한 리스트 생성
    kfold = KFold(n_splits = folds)
    scores = []
    
    # KFold 교차 검증 수행
    for iter_count, (train_index, test_index) in enumerate(kfold.split(X_titanic_df)) :
        # X_titanic_df 데이터에서 교차 검증별로 학습과 검증 데이터를 가리키는 index 생성
        X_train, X_test = X_titanic_df.values[train_index], X_titanic_df.values[test_index] # values를 통해 df를 ndarray로 변환
        y_train, y_test = y_titanic_df.values[train_index], y_titanic_df.values[test_index]
        
        # Classifier 학습/예측/평가
        clf.fit(X_train, y_train)
        clf_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, clf_pred)
        scores.append(accuracy)
        print("교차 검증 {0} 정확도 : {1:.4f}".format(iter_count, accuracy))
        
    # 5개의 fold에서 평균 계산
    mean_score = np.mean(scores)
    print("mean1평균 정확도: {0:.4f}".format(mean_score))

#함수호출
exec_kfold(dt_clf, folds = 5)

# 교차 검증 0 정확도 : 0.7542
# 교차 검증 1 정확도 : 0.7809
# 교차 검증 2 정확도 : 0.7865
# 교차 검증 3 정확도 : 0.7697
# 교차 검증 4 정확도 : 0.8202
# mean1평균 정확도: 0.7823
print()

from sklearn.model_selection import cross_val_score
scores = cross_val_score(dt_clf, X_titanic_df, y_titanic_df, cv = 5)
print("scores : ", scores)
for iter_count, accuracy in enumerate(scores) :
    print("교차 검증 {0} 정확도: {1:.4f}".format(iter_count, accuracy))
    
print("mean2평균 정확도: {0:.4f}".format(np.mean(scores)))
print()
# scores :  [0.74301676 0.7752809  0.79213483 0.78651685 0.84269663]
# 교차 검증 0 정확도: 0.7430
# 교차 검증 1 정확도: 0.7753
# 교차 검증 2 정확도: 0.7921
# 교차 검증 3 정확도: 0.7865
# 교차 검증 4 정확도: 0.8427
# mean2평균 정확도: 0.7879


# 왜 KFold를 이용했을 때의 accuracy와 cross_val_score를 이용했을 때의 accuracy가 다를까요? 
# 정답은 모델이 Classifier분류의 Statified KFold를 수행하기 때문입니다. 

# DecisionTreeClassfier 학습/예측평가
print('DecisionTreeClassifier 정확도 : {0:.4f}'.format(accuracy_score(y_test, dt_pred)))

# RandomForestClassifier 학습/예측/평가
print('RandomForestClassifier 정확도 : {0:.4f}'.format(accuracy_score(y_test, rf_pred)))

# LogisticRegression 학습/예측/평가
print('로직LogisticRegression 정확도 : {0:.4f}'.format(accuracy_score(y_test, lr_pred)))

print()