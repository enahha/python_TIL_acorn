'''
평균 제곱 오차 (Mean Square Error)
MSE는 이름에서도 알 수 있듯이 평균과 제곱를 이용해서 오차를 계산하는거예요.  
- 평균 제곱 오차 구하는 방법 - 
1. 평균을 구한다. 
2. 각 데이터에서 평균을 뺀 값에 제곱을 한다.
3. 2번에서 구한 값을 모두 더한다. 
4. 3번에서 구한 값에 총 데이터 숫자만큼 나눈다. 


한글로 최소자승법 또는 최소제곱법, 영어로는 LSM(Least Square Method) 또는 LMS(Least Mean Square) 방법.
최소자승법 하면 흔히 어떤 점들의 분포를 직선이나 곡선으로 근사하는 것만을 생각하기 쉽습니다.
 하지만, 최소자승법은 일반적인 
수학적 도구(tool)로서 수치해석, 회귀분석 뿐만 아니라 영상처리 분야에서도 다양하게 활용될 수 있습니다
'''

import numpy as np

import matplotlib 
import matplotlib.pyplot as plt
from matplotlib  import font_manager

import matplotlib as mpl # 음수 표시 에러 
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False

font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)
#---------------------------------------------------------------------------------------
# 점수를 y축, 시간을 x축
x = [2,4,6,8,10]      #총합계 30 /5   평균 6시간
y = [81,93,91,97,98]  #총합계 460 /5  평균 92점
mean_x = np.mean(x)
mean_y = np.mean(y)

parent = int( sum([(i-mean_x)**2      for i in x]) )
child = int( sum([ (x[idx]-mean_x) * (y[idx]-mean_y)  for idx,value in enumerate(x) ]) )
a = child/parent  #a=weight  y=ax+b
b = mean_y-(mean_x*a) 
print( 'parent =', parent) # parent = 40
print( 'child =', child)   # child = 76
print( 'a =', a)           # a = 1.9  a가중치=weight
                           # b=편향 92-(6*1.9) = 80.6
print( 'b =', b)           # b = 80.6        

print()
print('-' * 100)

result = [] #y=Ax+B
for i in range(5):
    cal = int((a*x[i]+b))
    # cal = (a*x[i]+b)
    result.append(cal)

print()
print( x )
print( y )
print( result) 
# 예상점수 [84, 88, 92, 95, 99]  cal = int((a*x[i]+b))
# 예상점수 [84.39999999999999, 88.19999999999999, 92.0, 95.8, 99.6]



x = [2,4,6,8,10]      #총합계 30 /5   평균 6시간
y = [81,93,91,97,98]  #총합계 460 /5  평균 92점

su = np.polyfit(x, y, 1)
print(su) #[ 1.9 80.6]
print()
y_pred = np.array(x) * su[0] + su[1] # x 값에 회귀를 진행한 예측 y 값

#스캐터 표시 plt.plot(x,y)
plt.plot(x, y_pred, color = 'b')
plt.scatter(x, y, color = 'r')
for i, v in enumerate(x):
    plt.text(v, y[i], y[i], fontsize = 9, color='green',
            horizontalalignment='center',  # horizontalalignment (left, center, right)
            verticalalignment='bottom')   # verticalalignment (top, center, bottom)
plt.show()

print()
print('-' * 100)