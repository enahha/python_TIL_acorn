import numpy as np

np.random.seed(1234)
print(np.random.rand(3,5))   # 3행 5열
print()
print(np.random.rand(150).reshape(30,5)) # 15개를 3 * 5열로

j = np.random.rand(3,5)
print('평균 : ', j.mean())
print('평균 : ', np.mean(j))

print('편차 : ', j.std())
print('편차 : ', np.std(j))

print('중앙 : ', np.median(j))

print('총점 : ', np.sum(j))

print('행총점 : ', np.sum(j, axis=1))   # 행
print('열총점 : ', np.sum(j, axis=0))   # 열

print('누적합(행별로 열 단위로 누적) : ', np.cumsum(j))   # 열