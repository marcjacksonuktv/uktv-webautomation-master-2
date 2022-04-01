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
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
testurl = 'https://uktvplay.uktv.co.uk/'
driver.get(testurl)
a = ActionChains(driver)
driver.implicitly_wait(15)

# Cookie Notice
CookieYes = driver.find_element_by_id('cookie-agree').click()

# Header
uktvplaylogo = driver.find_element_by_id('nav-bar-home')
categories = driver.find_element_by_id('nav-bar-categories')
channels = driver.find_element_by_id('nav-bar-channels')
boxsets = driver.find_element_by_id('nav-bar-boxsets')
a2z = driver.find_element_by_id('nav-bar-az')
more = driver.find_element_by_id('nav-bar-more')
mylist = driver.find_element_by_id('nav-bar-mylist')
account = driver.find_element_by_id('nav-bar-account')
search = driver.find_element_by_id('nav-bar-search')

# Sign In
account.click()
email = driver.find_element_by_id('email').send_keys('firefoxuser@testaccount.com')
password = driver.find_element_by_id('password').send_keys('password123')
SignIn_button = driver.find_element_by_id('sign-in-btn').click()
time.sleep(3)

#Search
Search = driver.find_element_by_id('nav-bar-search').click()
PopularSearch3 = driver.find_element_by_id('popular-result-1').click()
time.sleep(2)

# My List
addtofave = driver.find_element_by_id('add-to-favourites').click()
time.sleep(1)
mylist = driver.find_element_by_id('nav-bar-mylist').click()
time.sleep(5)
# insert screenshot here
removeshow = driver.find_element_by_id('Close-X').click()
time.sleep(2)
History = driver.find_element_by_id('tab-history').click()
time.sleep(2)

#Search
Search = driver.find_element_by_id('nav-bar-search').click()
PopularSearch3 = driver.find_element_by_id('popular-result-1').click()
time.sleep(2)

print ('My List Passed')