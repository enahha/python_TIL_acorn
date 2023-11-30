import pandas as pd

path = './data/emp.csv' 
emp = pd.read_csv(path, encoding='cp949')
print(emp)

print(emp.loc[2:5], ['Name', 'No', 'Pay'])      # 열을 이름으로 표시
print(emp.iloc[2:5, [1,0,2]])       # 열을 숫자로 표시