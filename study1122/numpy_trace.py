import numpy as np

# trace : 대각선의 합 출력

mat = np.arange(16).reshape(4,4) # 0~15
print(mat)
print('대각합 =',  np.trace(mat)) #30출력
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
대각합 = 0+5+10+15
'''

print()
print('np.trace() 3차원 대각연산')
import time
time.sleep(1)
mat = np.arange(27).reshape(3,3,3) # 0~26
print(mat)
print('대각합 =',  np.trace(mat)) # 36, 29, 42 결과값 출력 

'''
대각합 = [36 39 42] 결과값 보여주고 데이터추출 
36 = 0+12+24
39 = 1+13+25
42 = 2+14+26
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
대각합 = [36 39 42]
'''



print()
print('-' * 100)