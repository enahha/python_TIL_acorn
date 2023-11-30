import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)


name = [ 'kim', 'lee', '찰리', 'choi', 'young']
score =[ 40, 90, 35, 55, 85]
#라인 plt.plot(name, score) 
# plt.pie(score, labels=name)
plt.pie(score, labels=name, autopct='%.2f')
plt.title('pie 그래픽 연습')
# plt.legend(name, loc='upper right')
plt.show()







print()
print('-' * 100)

'''
  File "c:\Mtest\work1127\06matplotlib.py", line 1, in <module>
    import matplotlib
    ModuleNotFoundError: No module named 'matplotlib'
    우리는 수작업으로 설치  pip install  matplotlib 
'''