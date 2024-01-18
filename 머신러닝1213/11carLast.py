import matplotlib.pyplot as plt
from matplotlib import rc ,  font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import numpy as np
import cv2 

import warnings
warnings.filterwarnings('ignore') 


def preprocessing(car_no):
    image = cv2.imread('images/car/%02d.jpg' %car_no, cv2.IMREAD_COLOR)
    if image is None:
        return None, None
    
    plt.figure(figsize=(10,6))
    plt.imshow(image, cmap='gray')
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
car_no = 20
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

    chk1 = 3000 < (h * w) < 12000  
    chk2 = 2.0 < data < 6.5        
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
    crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) 
    return cv2.resize(crop_img, (144, 28))    
          
# 12-15-금요일 아래문장 주석처리 
# cd2 = find_car(morph) 
# imgs = [position_car(image, k) for k in cd2]
# for k, img in enumerate(imgs):
#   cv2.polylines(image, [np.int32(cv2.boxPoints(cd2[k]))], True, (0, 255,255), 2)

# cv2.imshow("image", image)
# cv2.waitKey(0)


def charnumber(image,center):
    h,w = image.shape[:2]
    fill = np.zeros((h+2, w+2) , np.uint8)
    dif1, dif2 = (25,25,25), (25,25,25) 
    flags = 4 + 0xff00 + cv2.FLOODFILL_FIXED_RANGE
    flags = flags + cv2.FLOODFILL_MASK_ONLY

    #후보영역에도 유사컬러 채우기
    rand = np.random.randint(-15,15, (20,2))
    rand = rand + center
    for x, y in rand:
        if 0<=x <w  and  0<=y <h:
            a,b,fill,d = cv2.floodFill(image, fill,(x,y), 255, dif1,dif2, flags)
    return cv2.threshold(fill, 120,250, cv2.THRESH_BINARY)[1]

cd2 = find_car(morph) 
fills = [charnumber(image,size) for size,x,y in cd2]
my = [find_car(fill) for fill in fills]
my = [cand[0] for cand in my  if cand]
imgs =  [ position_car(image,k) for k in my]
for k, img in enumerate(imgs):
  cv2.polylines(image, [np.int32(cv2.boxPoints(cd2[k]))], True, (255, 255, 0), 5)
  cv2.imshow('test', img)

cv2.imshow("image", image)
cv2.waitKey(0)


print()
print('11carLast.py문서 이미지 처리 종료 ')
print()