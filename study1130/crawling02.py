import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver=webdriver.Chrome(options=options)
# driver.set_window_size(1920, 1280)

#03webinterpark.py
url = 'https://mtravel.interpark.com/home'
driver.get(url)
time.sleep(1)


searchForm = driver.find_element(by=By.CLASS_NAME, value='searchForm')
driver.implicitly_wait(1)
searchForm.click()
input = searchForm.find_element(by=By.ID, value='txtHeaderInput')
input.send_keys('로마')
button = searchForm.find_element(by=By.ID, value='btnHeaderInput')
button.click()
driver.implicitly_wait(1)

found=driver.find_element(by=By.CSS_SELECTOR, value=".searchAllBox.overseaTravel.col1>.moreBtnWrap>.moreBtn")
found.click()

boxItems = driver.find_elements(by=By.CSS_SELECTOR, value='.searchAllBox.overseaTravel.col1>.boxList>li')
print()
time.sleep(1)

for bt  in boxItems:
    print('큰제목: ',   bt.find_element(by=By.CSS_SELECTOR, value='div.productInfo > div:nth-child(2) > div:nth-child(1) > a >h5').text )
    print(' ㄴ부제목: ', bt.find_element(by=By.CSS_SELECTOR, value='div.productInfo > div:nth-child(2) > div:nth-child(1) > p').text )
    print(' ㄴ가격: ',   bt.find_element(by=By.CSS_SELECTOR, value='div.productInfo > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > p > strong').text )
    print(' ㄴ그림: ',   bt.find_element(by=By.CSS_SELECTOR, value='img').get_attribute('src')) 
    print()




time.sleep(20)
print()
print('- ' * 100)

