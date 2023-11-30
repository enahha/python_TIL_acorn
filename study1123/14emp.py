import pandas as pd

path = './data/emp.csv' 
emp = pd.read_csv(path, encoding='cp949')
print(emp)
print()

print(emp.loc[3])
print()


print(emp.loc[2:5])  #loc[시작행:끝행 , 열]
print()

print(emp.loc[2:5 , ['Name','No', 'Pay']])  #loc[ 시행:끝행, ['Name','Pay'] ] 
print(emp.iloc[2:5 , [1,0,2]])  #loc[ 시행:끝행-1, [열표시를 숫자로가능] ] 
print()



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