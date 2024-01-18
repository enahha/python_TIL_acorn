
import time
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시 

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

#새로운 라이브러리 추가
import cv2

# ModuleNotFoundError: No module named 'cv2'
# 설치 pip install opencv-python 

#1번째 원본
img_ori = cv2.imread('./data/car.png',  cv2.IMREAD_COLOR)
height, width, channel = img_ori.shape

plt.figure(figsize=(10, 6))
plt.imshow(img_ori,cmap='gray') # cv2.IMREAD_COLOR
print()
print('height, width, channel 데이터값확인 ', height, width, channel)
plt.show()
time.sleep(1)

#2번째 HSV컬러변형
# gray = cv2.cvtColor(img_ori, cv2.COLOR_RGB2GRAY) #원본과 비슷
# gray = cv2.cvtColor(img_ori, cv2.COLOR_RGB2HSV) #블루색 더 강함 
# plt.figure(figsize=(10, 6))   
# plt.imshow(gray,cmap='gray')
# plt.show()
# time.sleep(1)


# 중요중요함 가우시안블러 - 사진의 노이즈 제거 
# Thresholding 이란 지정한 threshold 값을 기준으로 정하고
# 이보다 낮은 값은 0, 높은 값은 255로 변환한다. 즉 흑과 백으로만 사진을 구성
# Contours를 찾으려면 검은색 배경에 흰색 바탕이어야 함
# Contours란 동일한 색 또는 동일한 강도를 가지고 있는 영역의 경계선을 연결한 선

# #12-14-목요일 
# #3번째 Thresholding 글자번호를 기준으로  윤곽선표시 
gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
img_thresh = cv2.adaptiveThreshold(
    gray,
    maxValue=255.0,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY_INV,
    blockSize=19,
    C=9
)
plt.title('윤곽선 표시 Threshold 적용')
plt.imshow(img_thresh, cmap='gray')
plt.show()
time.sleep(1)

# #4번째 GauusianBlur적용해서 Thresholding 글자번호추출
# hsv = cv2.cvtColor(img_ori, cv2.COLOR_BGR2HSV)
# gray = hsv[:, :, 2]
# img_blur = cv2.GaussianBlur(gray, ksize=(5,5), sigmaX=0)
# img_blur_thresh = cv2.adaptiveThreshold(
#     img_blur,
#     maxValue=255.0,
#     adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     thresholdType=cv2.THRESH_BINARY_INV,
#     blockSize=19,
#     C=9
# )

# plt.title(' GaussianBlur')
# plt.imshow(img_blur_thresh, cmap='gray')
# plt.show()
# time.sleep(1)

## 4번째 가우시안블러 - 그림의 노이즈 제거 
# Contours를 찾으려면 검은색 배경에 흰색 바탕이어야 함
# Contours란 동일한 색 또는 동일한 강도를 가지고 있는 영역의 경계선을 연결한 선











print()
print('- ' * 70)
