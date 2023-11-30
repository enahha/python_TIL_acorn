import pandas as pd

path = './data/titanic.csv' 
tt = pd.read_csv(path, encoding='cp949')
print(tt) 
print()

path = './data/emp.csv' 
emp = pd.read_csv(path, encoding='cp949')
print(emp) 
print(emp.Name) #ok
# print(emp['Name']) #ok
# print(emp.name) #failed
print(emp.loc[3]) #까사노

'''
Name: Name, dtype: object
No      104
Name    까사노
Pay     350
Name: 3, dtype: object
''' 

'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  까사노  350
4  105  아이유  400
5  106  고길동  450
'''
print()
print('-' * 100)