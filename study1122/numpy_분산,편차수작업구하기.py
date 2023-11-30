import numpy as np

my = [ 179, 177, 175, 183, 181 ] #시험점수 총점=895 평균=179.0
data = np.array(my)
print('넘피총점 =', data.sum() )
print('넘피평균 =', data.mean() )
print('넘피평균 = ', np.mean(my))
