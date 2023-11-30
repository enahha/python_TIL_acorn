import pickle
import time

color = ['blue', '블루베리', 34343, '@#!@#@#!']
path = '../data/colors.plk'     #   확장자는 알아서
f = open(path, 'wb')
pickle.dump(color, f)

time.sleep(1)
print(path, '피클 저장 성공')