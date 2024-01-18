import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc ,  font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import cv2 
import sys
import time
import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시 

# path ='./data/scuba.mp4'
# cap = cv2.VideoCapture(path)

# path ='./data/36.jpg'
# img = cv2.imread(path)
# title = 'iu'
# x,y = 100, 100


# font = 'c:/windows/Fonts/malgun.ttf'
from PIL import ImageFont, ImageDraw, Image
font =  ImageFont.truetype('c:/windows/Fonts/malgun.ttf')


path ='./data/blank_500.jpg'
img = cv2.imread(path)
cv2.putText(img, 'winter test ', (30,70), cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC  ,2, (0,0,0))
cv2.putText(img, 'spring test ', (30,130), cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC  ,2, (0,0,0))
cv2.putText(img, 'python test ', (30,200), cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC  ,2, (0,0,0))
#에러 cv2.setText(img, 'HB winter', (30,70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0))
cv2.imshow('text test', img)

key = cv2.waitKey()  #일시정지역할 
# print(key, ' 문자출력키값 ' , chr(key))
# if key==ord('q') or key == 27 or key == 32 or key == ord('Q')  :
cv2.destroyAllWindows()
print('프로그램을 종료합니다')

print('08img.py문서 이미지 처리 종료 ')
print()