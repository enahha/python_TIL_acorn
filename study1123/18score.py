import pandas as pd 
#18score.py

path = './data/score.csv'
score = pd.read_csv(path, encoding='cp949')
print(score)
print()
# 문제 dept다음에 새로운열 5열tot=kor+eng+mat,  6열avg=tot/3
kor = score.kor
eng = score['eng']
mat = score['mat']
tot = kor+eng+mat
avg = round(tot/3,2)
score.insert(5, ['tot'], tot, True)
score.insert(6, ['avg'], avg, True)
print(score)







print()
print('-' * 100)