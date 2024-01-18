from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
import selenium
import time

# 나스닥 선물
# url = 'https://finance.daum.net/global/quotes/US.NDX'

url='https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=삼성전자'

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)

a1 = driver.find_element(By.XPATH, '//*[@id="comColl"]/div[3]/div/div[1]/div/span[2]').text
print('전체 : ', a1)
pos = a1.index('(')
print(a1[0:pos].replace('하락', '-'))

#=====================================

