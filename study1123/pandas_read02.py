import pandas as pd

path = './data/emp.csv' 
emp = pd.read_csv(path, encoding='cp949')
print(emp) 
print(emp.head())
print()
print(emp.tail())
print()
print(emp.head(3))
print('-' * 100)

print()
print(emp.info())
print()
print(emp.describe())
'''
               No         Pay
count    7.000000    7.000000
mean   104.000000  400.000000
std      2.160247  122.474487
min    101.000000  150.000000
25%    102.500000  375.000000
50%    104.000000  450.000000
75%    105.500000  475.000000
max    107.000000  500.000000
'''



print()
print('-' * 100)