import numpy as np


my = [ 179, 177, 175, 183, 181 ] #시험점수 총점=895 평균=179.0

print('일반총점 =', sum(my) )
print('일반평균 =', sum(my)/len(my) )
print('최대수 =', max(my) )
print('최소수 =', min(my) )
print()
#int(),float(),round(숫자,자릿수),sum(),len(),max(),min(),pow(숫자,2)

print('넘피총점 =', np.sum(my) )
print('넘피평균 =', np.mean(my) )
print()

avg = np.mean(my)
print(avg-my[0],avg-my[1],avg-my[2],avg-my[3],avg-my[4])
print('평균~점수차이 ', int(avg-my[0]+avg-my[1]+avg-my[2]+avg-my[3]+avg-my[4]) )

my = [ 179, 177, 175, 183, 181 ] #시험점수 총점=895 평균=179.0
data = np.array(my)
print('넘피총점 =', data.sum() )
print('넘피평균 =', data.mean() )




print()
print()
print('-' * 100)