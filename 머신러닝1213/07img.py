
import cv2 
import sys
import time
import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시 

# path ='./data/scuba.mp4'
# cap = cv2.VideoCapture(path)

path ='./data/36.jpg'
img = cv2.imread(path)
title = 'iu'
x,y = 100, 100

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0)
    print(key, ' 문자출력키값 ' , chr(key))
    if key==ord('q') or key == 27 or key == 32 or key == ord('Q')  :
        cv2.destroyAllWindows()
        print('프로그램을 종료합니다')
        break
    elif key == ord('h'): #왼쪽 -
        x = x-20
    elif key == ord('j'): #오른쪽 +
        x = x+20
    elif key == ord('l'): #윗쪽 -
        y = y-20
    elif key == ord('k'): #아래쪽 +
        y = y+20

print('07img.py문서 이미지 처리 종료 ')
print()