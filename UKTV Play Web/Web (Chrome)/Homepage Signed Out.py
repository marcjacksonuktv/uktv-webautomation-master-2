import sys
import time
from time import gmtime, strftime
import datetime
import conf as conf
import self as self
now = datetime.datetime.now()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

testurl = 'https://uktv:wemakegreattv@uktvplay.ppuktv.co.uk/'
driver.get(testurl)
a = ActionChains(driver)
driver.implicitly_wait(10)

# Cookie Notice
CookieYes = driver.find_element(By.ID, 'cookie-agree').click()
time.sleep(2)

# Header
uktvplaylogo = driver.find_element(By.ID, 'nav-bar-home')
categories = driver.find_element(By.ID, 'nav-bar-categories')
channels = driver.find_element(By.ID, 'nav-bar-channels')
boxsets = driver.find_element(By.ID, 'nav-bar-boxsets')
a2z = driver.find_element(By.ID, 'nav-bar-az')
more = driver.find_element(By.ID, 'nav-bar-more')
mylist = driver.find_element(By.ID, 'nav-bar-mylist')
account = driver.find_element(By.ID, 'nav-bar-account')
search = driver.find_element(By.ID, 'nav-bar-mylist')

# Featured Carousel / Signed Out Only

#FeaturedCarousel = driver.find_element(By.ID, 'featured-title-rp-2')
#if FeaturedCarousel.text:
 #   "Featured"
    #pass
    #print("Featured Carousel Present")

# Tab Through Page
a.send_keys(Keys.TAB * 85).perform()

print("Signed Out Homepage Passed")