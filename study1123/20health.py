import pandas as pd 
import time

# 20health.py

path = './data/health.csv'
health = pd.read_csv(path, encoding='cp949')
print(health)
print()

time.sleep(1)
print('----------- health[ (health.WEIGHT)==70] 테이터출력 11:47 -----------')
print(health[ (health.WEIGHT)==70]) #몸무게 70기준으로 추출 
data = health[ (health.WEIGHT)==70].index
remove = health.drop(data)
print(remove)

fname = './data/health.csv'
remove.to_csv(fname, index=False)
time.sleep(0.5)

print('(health.WEIGHT)==70 삭제여부확인')
path = './data/health.csv'
health = pd.read_csv(path, encoding='cp949')
print(health)

print()
print('-' * 100)