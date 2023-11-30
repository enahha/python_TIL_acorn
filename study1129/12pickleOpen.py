# 파이썬 피클 import pickle
# 파이썬 피클 pickle.dump()  저장
# 파이썬 피클 pickle.load()  열기

import pickle
import time


path ='./data/colors.pkl'
f = open(path, 'rb')
data = pickle.load(f)
print(data)
time.sleep(0.3)

print()
print(path, '피클오픈성공했습니다')







print()
print()
