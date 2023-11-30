import pandas as pd 
# 19health.py

path = './data/health.csv'
health = pd.read_csv(path, encoding='cp949')
print(health)
print()  # [861 rows x 7 columns]  

print('결측값 ', health.isnull().sum())
print('중복값 ', health.duplicated().sum())
print(health.tail())
print()
print(health[ (health.WEIGHT)==50]) #몸무게 50기준으로 추출 

# score.csv파일 dept필드에서 103출력 
# print(score[ score['dept']==103])
# print()
# print(score[ (score.dept)==102])
# print()


print()
print()
print('-' * 100)