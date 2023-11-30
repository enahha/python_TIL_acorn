import time
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver=webdriver.Chrome(options=options)

url = 'https://comic.naver.com/webtoon/detail?titleId=818205&no=3&week=tue'
driver.get(url)
time.sleep(2)
driver.execute_script('window.scrollTo(0, (document.body.scrollHeight)-2700);')

u_cbox_list = driver.find_element(by=By.CLASS_NAME, value='u_cbox_list')
comments = driver.find_elements(by=By.CLASS_NAME, value='u_cbox_comment')
print('comments타입 확인 ', type(comments))

u_nick = comments[5].find_element(by=By.CLASS_NAME, value='u_cbox_nick').text
u_content = comments[5].find_element(by=By.CLASS_NAME, value='u_cbox_contents').text
u_date = comments[5].find_element(by=By.CLASS_NAME, value='u_cbox_date').text
u_recomm = comments[5].find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text
print('1번째 댓글내용 ')
print('닉네임:{}  댓글:{} 날짜:{} 추천수:{}'.format(u_nick, u_content, u_date, u_recomm))
print('\nweb크롤링 빛나는 나나나나  test ')
time.sleep(15)
driver.close()


time.sleep(5)
print()
print('-' * 100)

