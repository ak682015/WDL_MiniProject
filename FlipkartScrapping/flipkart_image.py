# Create new Instance of Chrome in incognito modefrom bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import requests

##------------------------ changes in this part only --------------------------------- ##

driver = webdriver.Chrome(executable_path=r"D:\ArmanK\chromedriver.exe")
# driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/search?q=phones&marketplace=FLIPKART&otracker=start&as-show=on&as=off&page=3')

for i in range(25):
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(0.5)
    res = driver.execute_script("return document.documentElement.outerHTML")

# driver.quit()

soup = BeautifulSoup(res, 'lxml')

##------------------------ changes end here. Rest of the things are same. ------------------ ##

box = soup.find('div', {'class': '_3e7xtJ'})

all_div = box.find_all('div', {'class': '_3BTv9X'})

all_src = []
for all_img in all_div:
    img_type = all_img.find('img')
    img_type = img_type['src']
    all_src += [img_type]

final_src = []
for s in all_src:
    if '/312/312' in s:
        final_src += [s]

if not os.path.exists('MobileImages'):
    os.makedirs('MobileImages')

for j, srcs in enumerate(final_src):
    f = open('MobileImages\\phone' + str(j) + '.jpg', 'wb')
    f.write(requests.get(srcs).content)
    f.close()

driver.quit()
