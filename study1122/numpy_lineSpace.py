import numpy as np

x = np.linspace(0, 70, 5)   # 정밀도를 높이기 위해 실수형으로 나온다.(시, 끝, 갯수)
print(x)

x = np.linspace(0, 70, 10, endpoint=False, retstep=True)  
 # 정밀도를 높이기 위해 실수형으로 나온다. endpoint를 false로 설정해주면 정수로(시, 끝, 갯수)
print(x)
