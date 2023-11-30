import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver=webdriver.Chrome(options=options)
# driver.set_window_size(1920, 1280)

#04webdaum.py
url='https://www.daum.net'
driver.get(url)
time.sleep(1)


sel = driver.find_element(by=By.CLASS_NAME, value='searchForm')



time.sleep(20)
print()
print('- ' * 100)