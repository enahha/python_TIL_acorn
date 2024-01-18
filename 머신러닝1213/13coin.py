import matplotlib.pyplot as plt
from matplotlib import rc ,  font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import numpy as np
import cv2 

import warnings
warnings.filterwarnings('ignore') 

# 순서1]
def preprocessing(car_no):
    image = cv2.imread('./coin/%02d.png' %car_no, cv2.IMREAD_COLOR)
    print('image 정보 숫자로 출력 ')
    print(image)
    if image is None:
        return None, None
    cv2.imshow('1 test ', image)
    cv2.waitKey()
    # plt.figure(figsize=(10,6))
    # plt.imshow(image)
    # plt.show()

    # kernel = np.ones( (5,13), np.uint8) #마스크용 사용
    # gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray=cv2.blur(gray, (5,5))
    # gray=cv2.Sobel(gray, cv2.CV_8U, 1,0,3) 
    # thres=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)[1]
    # morph=cv2.morphologyEx(thres,cv2.MORPH_OPEN,kernel,iterations=3)
    # return  image, morph

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          # 명암도 영상 변환
    gray = cv2.GaussianBlur(gray, (7,7), 2, 2)              # 블러링
    flag = cv2.THRESH_BINARY + cv2.THRESH_OTSU              # 오츠(otus) 이진화 지정
    _, th_img = cv2.threshold(gray, 130, 255, flag)         # 이진화

    mask = np.ones((3,3), np.uint8)
    th_img = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask) # 열림 연산
    return image, th_img


# 순서2]
def find_coins(image):
    results = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = results[0] if int(cv2.__version__[0]) >= 4 else results[1]

    circles = [cv2.minEnclosingCircle(c) for c in contours] # 외각 감싸는 원 검출
    circles = [(tuple(map(int, center)), int(radius))
               for center, radius in circles if radius>25]
    return circles


# 순서3]
def make_coin_img(src, circles):
    coins = []
    for center, radius in circles:
        r = radius * 3                                      # 검출 동전 반지름 3배
        cen = (r // 2, r // 2)                              # 마스크 중심
        mask = np.zeros((r,r,3), np.uint8)                  # 마스크 행렬
        cv2.circle(mask, cen, radius, (255,255,255), cv2.FILLED)
        coin = cv2.getRectSubPix(src, (r,r), center)        # 동전 영상 가져오기
        coin = cv2.bitwise_and(coin, mask)                  # 마스킹 처리
        coins.append(coin)                                  # 동전 영상 저장장
    return coins


# 순서4] cals_histo_hue색상(coin)
def cals_histo_hue(coin):
    hsv = cv2.cvtColor(coin, cv2.COLOR_BGR2HSV)
    hsize, ranges = [32], [0,180] #색상의 화소범위 0~180
    ret = cv2.calcHist( [hsv], [0], None, hsize, ranges)
    return ret.flatten()


# 순서5] grouping(hist)  넘피.multiply(), np.sum()
def grouping(hist):
    # ws = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3,
    #       4, 5, 6, 8, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0] 
    ws = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    sim = np.multiply(hist, ws)
    ret = np.sum(sim, axis=1)/np.sum(hist, axis=1) 
    groups = [1 if s>1.2 else 0 for s in ret]
    return groups


# 순서6] classify_coins(서클, 그룹) 1월 10원 50원 100원 500원
def classify_coins(circles, groups):
    ncoins = [0] * 4
    coin_class = []
    g = np.full( (2,70), -1 )
    # g = np.full( (2,70) , -1 , np.int_ )
    g[0, 26:47],  g[0, 47:50],  g[0, 50:] = 0, 2, 3  #10원 
    g[1, 36:44],  g[1, 44:50],  g[1, 50:] = 1, 2, 3  #50원 100원 

    for group, (a,radius) in zip( groups, circles):
        coin = g[group,radius]
        coin_class.append(coin)
        ncoins[coin] = ncoins[coin]  + 1

    return np.array(ncoins), coin_class

# 순서1 ~ 순서3  이미완성
# 순서4] cals_histo_hue색상(coin)
# 순서5] grouping(hist)  넘피.multiply(), np.sum()
# 순서6] classify_coins(서클, 그룹) 1월 10원 50원 100원 500원
# 순서7] 동전금액표시 put_string(1,2,3,4,5) putText함수

#시작점 진입문서
coin_no = 2   #   79  int(input('12-18-월요일 이미지 번호(01~86)>>>  '))
image, th_img = preprocessing(coin_no)                  # 전처리 수행
circles = find_coins(th_img)                            # 객체(중심점, 반지름) 검출
coin_imgs = make_coin_img(image, circles)               # 개별 동전 영상 생성

#기술한 함수의 매개인자하고 리턴값 받기
coin_hue =[ cals_histo_hue(coin) for coin in coin_imgs]
groups = grouping(coin_hue)
color = [ (0,0,255), (255,255,0), (0,250,0), (250, 0, 250)]
ncoins, coin_class = classify_coins(circles, groups)

for i, (c,r) in enumerate(circles):
    cv2.circle(image, c,r, color[coin_class[i]], 2)
cv2.imshow('2 test ', image) #동전외곽선 컬러 표시
cv2.waitKey()

coin_value = np.array([10,50,100,500])
print()
for i in range(4):
    print('%3d원:  %3d개 ' %(coin_value[i], ncoins[i]))

total = sum( coin_value* ncoins)
string  = 'Total coin {:,} won'.format(total)
print( 'Total coin {:,} won'.format(total))

def put_string(frame, text, pt, value, color=(120,120,90)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    print('frame =', frame)
    text = text + str(value)

    # shade = (pt[0]+ 2 , pt[1] +2)
    # cv2.putText(frame, text, shade, font, 0.7, (100,100,100), 2) 
    cv2.putText(frame, text, pt, font, 0.7, color, 2) 

# 참고 cv2.putText(img, '1 winter test ', (30,70), cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC  ,2, (0,0,0))
put_string(image, string, (700,50), ' ', (0,250,0) ) #오른쪽상단에 금액표시

color = [ (0,0,255), (255,255,0), (0,250,0), (250, 0, 250)]
for i, (c,r) in enumerate(circles):
    cv2.circle(image, c,r, color[coin_class[i]], 3)
    put_string(image, str(coin_value[coin_class[i]]), (c[0], c[1]+15), '', color[3])
cv2.imshow('3 last test ', image)
cv2.waitKey()

# 순서1 ~ 순서3  이미완성
# 순서4] cals_histo_hue색상(coin) 완성
# 순서5] grouping(hist)  넘피.multiply(), np.sum() 완성
# 순서6] classify_coins(서클, 그룹) 1월 10원 50원 100원 500원 완성
# 순서7] 동전금액표시 put_string(1,2,3,4,5) putText함수

#순서1] 코인이미지 높이, 길이, 채널 정보확인 
# coin_no = int(input("코인 번호 (0~86)>>>  ")) 
# coin_no =  './coin/47.png'
# img = cv2.imread(coin_no)
# height, width, channel = img.shape 
# print('img.shape 정보', img.shape)
# print('width=',width, 'height=', height,  'channel =', channel )
# cv2.imshow('test ', img)
# cv2.waitKey()


print()
print('13coin.py문서 이미지 처리 종료 ')
print()