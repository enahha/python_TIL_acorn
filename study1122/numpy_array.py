import numpy as np

# array가 하나일 때 ( [] )
# np는 array안의 array를 만들 때 np.array( [ [],[],[],.... ] )
su = np.array( [ [1,2,3], [4,5,6], [7,8,9], [10,11,12] ] )
print(su.shape)     # (4, 3)  4행 3열
print(su.dtype)     # int64
print(su.size)      # 12
print(su)