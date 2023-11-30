import pandas as pd

path = './data/score.csv' 
emp = pd.read_csv(path, encoding='cp949')

# 새로운 5열 tot , 6열 avg 추가
