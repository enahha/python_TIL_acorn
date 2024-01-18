
import cv2 
import sys
import time
import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시 


cap = cv2.VideoCapture(0)
try:
    if cap.isOpened():
        while True:
            ret, img = cap.read()
            print('ret =', ret, ' img =', img)
            print()
            if ret:
                cv2.imshow('camera', img)
                if cv2.waitKey(1) != -1 :
                    cv2.imwrite('./picture/rain.jpg', img)
                    print('rain.jpg 파일저장성공')
                    break
            else:
                print('카메라 작동 인식 실패 ')
                break
    else:
        print('isOpened() 아니면  ')



except Exception as ex:
    print('++++++++++++++++++++++++ 에러이유  ', ex)

# cap.release()
# print('12video_camera.py문서 종료 ')
print()
