import numpy as np

print('중복체크 unique(), set()')

a = np.array([5,4,3,1,2,3,4,3,3,3,1,2,1,2,5,1,2,3,1,2,2,1,3])
print(a)
print(np.unique(a)) #set역할 유니크개념은 db에서 pk키값

data = [5,4,3,1,2,3,4,3,3,3,1,2,1,2,5,1,2,3,1,2,2,1,3]
print(data)
print(set(data)) #set데이터복합응용 로또난수 
print('-' * 100)
print()


a = np.array([5,4,3,1,2,3,4,3,3,3,1,2,1,2,5,1,2,3,1,2,2,1,3])
b = np.array([ 0,0,0,7,8,1,0,0,0,9,6,0,0,0,0,0])
print(np.trim_zeros(b)) #앞뒤 0숫자 제거
print(np.trim_zeros(b,trim='f')) 
print(np.trim_zeros(b,trim='b'))
print()
print(np.full((4,6),91)) 



print()
print('-' * 100)