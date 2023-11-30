import numpy as np

mat = np.array( [ [1, 2],[2, 3] ] )
print( np.dot(mat, mat) )
'''
결과__
[[ 5  8]            >>> 1 x 1 + 2 x 2 ,,,, 1 x 2 + 2 x 3
 [ 8 13]]           >>> 2 x 1 + 3 x 2 ,,,, 2 x 2 + 3 x 3 
'''

mat_1 = np.array( [ [1,2], [2,3]] )
print( np.dot(mat_1, mat_1)) #[[5  8] [8 13]]
print()
print(mat_1.dot(mat_1))     #[[ 5  8] [ 8 13]]
print()

data = np.array( [[5,4],[2,3]] )
print( np.dot(data, data)) #[[33  32] [16 17]]
print()
print(data.dot(data))      #[[33  32] [16 17]]
print()



# 곱하기 참고하세요
# mat_1=np.array( [ [1,2], [2,3]] )
# print(mat_1)
# print()
# print(mat_1*mat_1) # [ [1 4]  [4 9] ]
# print()
