
import time
import numpy as np
import pandas as pd
import sys
import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시 

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import matplotlib.pyplot as plt

import matplotlib.cbook as cbook
import matplotlib.patches as patches

# C:\Users\hbi\anaconda3\envs\ck\Lib\site-packages\matplotlib\mpl-data\sample_data\36.jpg
# with cbook.get_sample_data('36.jpg') as image_file:
#     image = plt.imread(image_file)

# fig, ax = plt.subplots()
# im = ax.imshow(image)
# patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
# im.set_clip_path(patch)
# ax.axis('off')
# plt.show()



#새로운 라이브러리 추가
import cv2
image = cv2.imread('./data/plane.jpg',  cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR
print('image데이터값 표시  ', image)
print()
plt.imshow(image)
plt.show()
time.sleep(1)

image_blur = cv2.blur(image, (20,20)) # 20 x 20 커널 평균값으로 이미지를 흐리게 함 
plt.imshow(image_blur, cmap='gray')
plt.show()
time.sleep(1)


image = cv2.imread('./data/plane.jpg', cv2.IMREAD_GRAYSCALE)

# 커널 생성(대상이 있는 픽셀을 강조)
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# 커널 적용 
image_sharp = cv2.filter2D(image, -1, kernel)

fig, ax = plt.subplots(1,2, figsize=(10,5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')

ax[1].imshow(image_sharp, cmap='gray')
ax[1].set_title('Sharp Image')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()  # 메모리 초기화

ch = cv2.waitKey(1)
if ch == 32 or ch == 27:  #대소문자 q/Q 클릭하면 종료, 일반적인 창닫기 x
    print('프로그램을 종료합니다 ')
    sys.exit()
    





print()
print('- ' * 70)
