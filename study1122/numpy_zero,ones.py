import numpy as np

a = np.zeros(7)
print(a, '\n')

b = np.zeros( (3, 5) )  # == np.zeros( [3, 5] ) ,3 행 * 5 열
print(b, '\n')

c = np.zeros(shape=(8, 2))  # 8 행 * 2 열
print(c, '\n')

a1 = np.ones(7)
print(a1, '\n')

b1 = np.ones( (3, 5) )  # == np.ones( [3, 5] ) ,3 행 * 5 열
print(b1, '\n')

c1 = np.ones(shape=(8, 2))  # 8 행 * 2 열
print(c1, '\n')