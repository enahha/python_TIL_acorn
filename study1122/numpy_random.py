import numpy as np

a = np.random.rand(15)      # 15개의 랜덤한 난수를 생성
print(a , '\n')

a1 = np.random.rand(15).reshape(5, 3)      # 15개의 랜덤한 난수를 생성후 5행 3열로 정렬
print(a1, '\n')

a2 = np.random.rand(3, 5)      # 5행 3열로 15개의 랜덤한 난수를 생성
print(a2, '\n')

a3 = np.random.randn(3, 5)      # 5행 3열로 15개의 랜덤한 난수를 생성 , (음수 0 양수) 랜덤
print(a3, '\n')

b = np.random.randint(0,5) # 하나 추출 1~5 앞
print(b)