import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc ,  font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import numpy as np
import cv2 

import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시 


# 전처리에서 모폴로지함수 적용하면 이미지침식,팽창,열기,닫기 ==>노이즈제거, 돌출완화
# cv2.MORPH_CLOSE, cv2.MORPH_OPEN, cv2.MORPH_DILAE, cv2.MORPH_ERODE
def preprocessing(car_no):
    image = cv2.imread('images/car/%02d.jpg' %car_no, cv2.IMREAD_COLOR)
    if image is None:
        return None, None
    
    plt.figure(figsize=(10,6))
    plt.imshow(image)
    plt.show()
    kernel = np.ones( (5,13), np.uint8) #마스크용 사용
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray=cv2.blur(gray, (5,5))
    gray=cv2.Sobel(gray, cv2.CV_8U, 1,0,3) 
    thres=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)[1]
    morph=cv2.morphologyEx(thres,cv2.MORPH_CLOSE,kernel,iterations=3)
    return  image, morph

#순서1] 이미지에 엣지를 구해서 필터적용 
# car_no = int(input("자동차 영상 번호 (0~15)>>>  ")) 
car_no = 20 # 5 1  13
image, morph = preprocessing(car_no) #데이터회색,블러
print('12-15-금요일 image = preprocessing(car_no')
print(image)
# print('morph = preprocessing(car_no) ', morph)

#순서2] 숫자영역 추출   번호판 크기 3000 ~ 12000 
def verify_size(size):
    w, h = size
    data = 0

    if h == 0 or w == 0: return False
    
    if h > w: 
        data = h / w 
    else:
        data = w / h  

    chk1 = 3000 < (h * w) < 12000  # 번호판 넓이 조건
    chk2 = 2.0 < data < 6.5        # 번호판 종횡비 조건
    return (chk1 and chk2)


def find_car(image):
    result = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   
    contours = result[0] 
    rects = [cv2.minAreaRect(c)  for c in contours] #최소사각형 지정 번호숫자가져오기 위한 
    cd = [ (tuple(map(int,center)), tuple(map(int,size)) ,angle )  for center,size,angle in rects  if verify_size(size)]      
    return cd



#순서3] 이미지 번호위치 문자지정
def position_car(image, rect):
    print('position_car함수호출')
    center, (w, h), angle = rect       # 중심점, 크기, 회전 각도
    if w < h :                         # 세로가 긴 영역이면
        w, h = h, w                    # 가로와 세로 맞바꿈
        angle -= 90                    # 회전 각도 조정

    size = image.shape[1::-1]           
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1) 
    rot_img= cv2.warpAffine(image, rot_mat, size, cv2.INTER_CUBIC)  
    crop_img = cv2.getRectSubPix(rot_img, (w, h), center)  
    crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)  # 명암도 영상
    return cv2.resize(crop_img, (144, 28))    
          

cd2 = find_car(morph) #이미지컨투어 사각형 지정 
imgs = [position_car(image, k) for k in cd2]
for k, img in enumerate(imgs):
  #  RGB=레드그린블루  cv2에서 BGR
  cv2.polylines(image, [np.int32(cv2.boxPoints(cd2[k]))], True, (0, 255,255), 2)

cv2.imshow("image", image)
cv2.waitKey(0)


# path ='./images/car/05.jpg'
# img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# dx = cv2.Sobel(img, -1, 1, 0)
# dy = cv2.Sobel(img, -1, 0, 1)

# # cv2.imshow(' 원본 ', img)
# cv2.imshow(' dx Sobel ', dx)
# cv2.imshow(' dy Sobel ', dy)
# plt.show()
# cv2.waitKey()
# cv2.destroyWindow()

print()
print('09car.py문서 이미지 처리 종료 ')
print()