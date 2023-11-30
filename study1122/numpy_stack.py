import numpy as np


a = np.array( [ [1,2], [3,4]] )
b = np.array( [ [5,6], [7,8]] )
print(np.vstack((a,b))) # [1 2] [3 4] [5 6] [7 8]
print(np.hstack((a,b))) # [1 2 5 6] [3 4 7 8] 
print('- ' * 100 )
print()

print(np.concatenate((a,b), axis=0)) #np.vstack((a,b)) axis=0  
print(np.concatenate((a,b), axis=1)) #np.hstack((a,b)) axis=1

'''
axis = 0
[[1 2]
 [3 4]]
[[5 6]
 [7 8]]

axis = 1
 [[1 2 5 6]
 [3 4 7 8]]
'''
'''
- 결합할 축(차원)을 지정 : 인수 axis
    -기본적으로 axis=0이다. 2차원 배열의 경우에는 새로운 축(0차원째)에 대해 결합이 이뤄지므로 세로로 결합
     axis = 1로 지정하면 2번째의 축(1차원째)이 열이므로 가로로 결합된다.
- numpy.stack()으로 새로운 축(차원)에 따른 결합
- numpy.block()으로 배치를 지정하여 결합
- numpy.vstack()으로 세로로 결합
- numpy.hstack()으로 가로로 결합
- numpy.dstack()으로 깊이 방향으로 결합
'''




print()
print('-' * 100)