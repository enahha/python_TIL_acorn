import pandas as pd

path = './data/emp.csv' 
emp = pd.read_csv(path, encoding='cp949')
print(emp)
print()

print( emp.loc[2:5 , ['Name','No', 'Pay']] )   # loc[ 시행:끝행, ['Name','Pay'] ] 
print( emp.iloc[2:5, [1, 0, 2]] )              # iloc[ 시행:끝행-1, [열표시를 숫자로가능] ] 
#15emp.py문서 16emp.py문서 코드구현 동일 






print()
print('-' * 100)