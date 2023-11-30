import time
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver=webdriver.Chrome(options=options)

#05webcsv.py
url = 'https://comic.naver.com/webtoon/detail?titleId=818205&no=3&week=tue'
driver.get(url)
time.sleep(2)
driver.execute_script('window.scrollTo(0, (document.body.scrollHeight)-2700);')

u_cbox_list = driver.find_element(by=By.CLASS_NAME, value='u_cbox_list')
comments = driver.find_elements(by=By.CLASS_NAME, value='u_cbox_comment')
print('체크체크 comments타입 확인 ', type(comments))
print()

path = './data/navercm.txt'
cmFile = open(path, mode='w', encoding='utf-8')

pathcsv = './data/navercm.csv'
result = []

for ct in comments:
    u_nick = ct.find_element(by=By.CLASS_NAME, value='u_cbox_nick').text
    u_content = ct.find_element(by=By.CLASS_NAME, value='u_cbox_contents').text
    u_date = ct.find_element(by=By.CLASS_NAME, value='u_cbox_date').text
    u_recomm = ct.find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text
    print('- ' * 70)
    print('닉네임:{}  댓글:{} 날짜:{} 추천수:{}'.format(u_nick, u_content, u_date, u_recomm))
    cmFile.write(u_nick+' '+u_content+' '+u_date+' '+u_recomm+'\n')
    result.append([u_nick] + [u_recomm ])
    
    
n_table = pd.DataFrame( result, columns=('nick', 'recomm'))
n_table.to_csv(pathcsv, encoding='cp949', mode='w', index=True)

time.sleep(15)
driver.close()
print(path + ' 텍스트파일 저장 성공했습니다')
print(pathcsv + ' 엑셀 csv파일 저장 성공했습니다')
cmFile.close()
# 현재문서 csv파일저장 
# 파이썬기초 파일처리 - txt,피클,csv
# 판다스를 이용해서 csv파일열기,저장
# 월요일, 화요일  지도맵
# 화요일  그래프  - matplotlib, seaborn
# 수요일   selenium의 웹드라이버 drirver.get(url주소)





time.sleep(5)
print()
print('-' * 140)

