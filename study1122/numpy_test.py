from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

id = "아이디"
pw = "비번"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # 브라우저 창을 최대화하는 옵션 추가

service = Service(r"크롬드라이버설치경로")
driver = webdriver.Chrome(service=service, options=chrome_options)