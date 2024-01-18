
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