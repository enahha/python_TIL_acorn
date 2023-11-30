import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

from matplotlib import rc
from matplotlib import font_manager


font_name = font_manager.FontProperties(fname='/Users/j.ena/Library/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

# pip install  matplotlib 설치 
print('차트 그래프 시작 ')
name = [ 'kim', 'lee', '찰리', 'chor', 'young']
score =[ 40, 90, 35, 55, 85]
plt.plot(name, score)
plt.title('첫번째 그래픽 연습 11-27-월요일 3:27')
plt.show()
time.sleep(1)

# plt.plot(name, score) 기본모양은  LINE 그래프임.
# 바 모양의 그래프를 그리고 싶으면 = blt.bar(x,y, width=)

# bar graph test
x = range(10)
y = np.random.randint(10,100,10)
plt.bar(x, y, width=0.9)
plt.title('bar graph test')
plt.show()
time.sleep(1)

# hist graph test
z = np.random.randn(10000) # 음수, 양수
plt.hist(z, bins=20, color='hotpink')
plt.title('hist graph test')
plt.show()



'''
  pip install  matplotlib 
'''
