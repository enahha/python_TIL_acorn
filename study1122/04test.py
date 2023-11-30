import numpy as np

x = [ 5,7,3 ]
y = [ 2,9,4 ]

# 에러 print(x*y)
a = np.array(x)
b = np.array(y)
print('곱하기연산 ' , a*b) #[10 63 12]

data = np.array(
    ( [[0, 1, 2, 3],[4, 5, 6, 7]],
      [[0, 1, 2, 3],[4, 5, 6, 7]],
      [[0 ,1 ,2, 3],[4, 5, 6, 7]] )
)




# 소트예제
# a = np.array([9, 1, 5, 3, 7, 4, 6, 8])
# print(a)
# print(np.sort(a)) #넘피라이브러리 소트 
# data=[9, 1, 5, 3, 7, 4, 6, 8]
# data.sort() #파이썬의 리스트의 소트
# print(data) 
# print()


print()
print('-' * 100)