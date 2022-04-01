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
from selenium.webdriver.common.by import By
from webdriver_manager.opera import OperaDriverManager
driver = webdriver.Opera(executable_path=OperaDriverManager().install())
testurl = 'https://uktv:wemakegreattv@uktvplay.uatuktv.co.uk/'
a = ActionChains(driver)
driver.implicitly_wait(15)

# Cookie Notice
CookieYes = driver.find_element(By.ID, 'cookie-agree').click()

# Header
uktvplaylogo = driver.find_element(By.ID, 'nav-bar-home')
categories = driver.find_element(By.ID, 'nav-bar-categories')
channels = driver.find_element(By.ID, 'nav-bar-channels')
boxsets = driver.find_element(By.ID, 'nav-bar-boxsets')
a2z = driver.find_element(By.ID, 'nav-bar-az')
more = driver.find_element(By.ID, 'nav-bar-more')
mylist = driver.find_element(By.ID, 'nav-bar-mylist')
account = driver.find_element(By.ID, 'nav-bar-account')
search = driver.find_element(By.ID, 'nav-bar-search')

# Sign In
account.click()
email = driver.find_element(By.ID, 'email').send_keys('operauser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('password123')
SignIn_button = driver.find_element(By.ID, 'sign-in-btn').click()
time.sleep(3)

# Channel dropdown menu
Channeldropdown = driver.find_element(By.ID, 'nav-bar-channels').click()
time.sleep(2)
davedropdown = driver.find_element(By.ID, 'nav-bar-dave')
davedropdownlink = davedropdown.get_attribute('href')
print(davedropdownlink)
davedropdown.click()

# --- scroll page ---
Davetvguide = driver.find_element(By.ID, 'tv-guide').click()
time.sleep(2)
driver.get(davedropdownlink)
time.sleep(2)
# --- scroll page ---
scrollpage=driver.find_element(By.TAG_NAME,'body')
scrollpage.send_keys(Keys.END)

Watchlivedave = driver.find_element(By.ID, 'on-now').click()
driver.implicitly_wait(7)