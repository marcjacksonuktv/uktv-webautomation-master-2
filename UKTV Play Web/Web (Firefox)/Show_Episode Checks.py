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

driver.execute_script("window.scrollTo(0, 700)")
time.sleep(2)

#Click Episodes on TV Tab
EpsonTV = driver.find_element_by_id('tab-tv').click()
time.sleep(2)
#Click Episodes on Demand Tab
EpsonDemand = driver.find_element_by_id('tab-vod').click()


#Click On Series drop down
SeriesDropdown = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]').click()
time.sleep(2)
#Click On Series1 drop down
Series1 = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]/div[2]/div[1]').click()
SeriesDropdown = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]').click()
time.sleep(2)
#Click On Series2 drop down
Series2 = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]/div[2]/div[2]').click()
SeriesDropdown = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]').click()
time.sleep(2)
#Click On Series3 drop down
Series3 = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]/div[2]/div[3]').click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 1500)")
time.sleep(2)

#Click Additional episodes
AdditonalEp1 = driver.find_element_by_id('undefined-1').click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 1500)")
time.sleep(2)

AdditonalEp2 = driver.find_element_by_id('undefined-2').click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 1700)")
time.sleep(2)
#More like this carousel shows