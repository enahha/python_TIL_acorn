import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc ,  font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import numpy as np
import cv2 

import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시 


#순서1] 이미지에 엣지를 구해서 필터적용 
# car_no = int(input("자동차 영상 번호 (0~15)>>>  ")) 
path = './images/car/12.jpg'
img = cv2.imread(path)
height, width, channel = img.shape 
print('img.shape 정보', img.shape)
print('width=',width, 'height=', height,  'channel =', channel )
cv2.imshow('test ', img)
cv2.waitKey()

path ='./images/car/05.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
dx = cv2.Sobel(img, -1, 1, 0)
dy = cv2.Sobel(img, -1, 0, 1)

# cv2.imshow(' 원본 ', img)
cv2.imshow(' dx Sobel ', dx)
cv2.imshow(' dy Sobel ', dy)
plt.show()
cv2.waitKey()





print()
print('10car.py문서  ')
print()