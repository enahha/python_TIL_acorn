import numpy as np

# 05ndim.py  : 배열의 차원 수 or 배열의 축 수
data = np.array(
    ( [[0, 1, 2, 3],[4, 5, 6, 7]],
      [[0, 1, 2, 3],[4, 5, 6, 7]],
      [[0 ,1 ,2, 3],[4, 5, 6, 7]] )
)

print(data, '\n')
print(' ' , data.ndim)  #3  3차원 배열
print(' ' , data.size)  #24
print(' ' , data.shape) # (3, 2, 4)   3 x 2의 4개의 항




print()
print('-' * 100)