import numpy as np

x = np.eye(7)       # 7*7, 대각으로 1이 채워지고 그 외는 0이 채워짐
print(x, '\n')

y = np.identity(7)  # 위와 결과값 동일
print('identity\n', y)