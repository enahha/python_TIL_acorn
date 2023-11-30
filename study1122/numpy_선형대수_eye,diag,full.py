import numpy as np

x = np.eye(7)       # 7*7, 대각으로 1이 채워지고 그 외는 0이 채워짐
print(x)
'''
[[1. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 1.]]
'''

# diag = 대각
y = np.diag( [71, 89, 23, 98, 56, 48] )
print(y)
'''
[[71  0  0  0  0  0]
 [ 0 89  0  0  0  0]
 [ 0  0 23  0  0  0]
 [ 0  0  0 98  0  0]
 [ 0  0  0  0 56  0]
 [ 0  0  0  0  0 48]]
'''
# full
z = np.full( (4,6), 51 )    # 4행 * 6 열 51 숫자 채워짐
print(z)