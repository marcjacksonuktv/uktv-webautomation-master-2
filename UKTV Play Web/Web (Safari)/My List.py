import sys
import time
from time import gmtime, strftime
import datetime
import conf as conf
import self as self
now = datetime.datetime.now()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = Options()
from selenium import webdriver
driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
testurl = 'https://uktvplay.uktv.co.uk/'
a = ActionChains(driver)
driver.get(testurl)
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
time.sleep(2)
# Sign In
account.click()
email = driver.find_element(By.ID, 'email').send_keys('safariuser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('Password123!!')
SignIn_button = driver.find_element(By.ID, 'sign-in-btn').click()
time.sleep(3)

#Search
Search = driver.find_element(By.ID, 'nav-bar-search').click()
PopularSearch3 = driver.find_element(By.ID, 'search-result-1').click()
time.sleep(2)

# My List
addtofave = driver.find_element(By.ID, 'add-to-favourites').click()
time.sleep(1)
mylist = driver.find_element(By.ID, 'nav-bar-mylist').click()
time.sleep(5)
# insert screenshot here
#removeshow = driver.find_element(By.ID, 'Close-X').click()
time.sleep(2)
#HistoryTab = driver.find_element(By.ID, 'tab-history').click()
#time.sleep(2)

#Search
Search = driver.find_element(By.ID, 'nav-bar-search').click()
PopularSearch3 = driver.find_element(By.ID, 'search-result-1').click()
time.sleep(2)

print ('My List Passed')