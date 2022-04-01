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

testurl = 'https://uktvplay.uktv.co.uk/'
# https://uktv:wemakegreattv@uktvplay.ppuktv.co.uk/
driver.get(testurl)
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
email = driver.find_element(By.ID, 'email').send_keys('chromeuser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('Password123!!')
SignIn_button = driver.find_element(By.ID, 'sign-in-btn').click()
time.sleep(3)

#Search
Search = driver.find_element(By.ID, 'nav-bar-search').click()
PopularSearch3 = driver.find_element(By.ID, 'search-input').send_keys('The')
time.sleep(2)
driver.get('https://uktvplay.uktv.co.uk/shows/the-architecture-the-railways-built/watch-online')
time.sleep(2)

driver.execute_script("window.scrollTo(0, 700)")
time.sleep(2)

#Click Episodes on TV Tab
EpsonTV = driver.find_element(By.ID, 'tab-tv').click()
time.sleep(2)
#Click Episodes on Demand Tab
EpsonDemand = driver.find_element(By.ID, 'tab-vod').click()


#Click On Series drop down
SeriesDropdown = driver.find_element(By.XPATH, '//*[@id="episodes-listings"]/div/section/div/div[1]').click()
time.sleep(2)
#Click On Series1 drop down
Series1 = driver.find_element(By.XPATH, '//*[@id="episodes-listings"]/div/section/div/div[1]/div[2]/div[1]').click()
SeriesDropdown = driver.find_element(By.XPATH, '//*[@id="episodes-listings"]/div/section/div/div[1]').click()
time.sleep(2)
#Click On Series2 drop down
Series2 = driver.find_element(By.XPATH, '//*[@id="episodes-listings"]/div/section/div/div[1]/div[2]/div[2]').click()
SeriesDropdown = driver.find_element(By.XPATH, '//*[@id="episodes-listings"]/div/section/div/div[1]').click()
time.sleep(2)
#Click On Series3 drop down
Series3 = driver.find_element(By.XPATH, '//*[@id="episodes-listings"]/div/section/div/div[1]/div[2]/div[3]').click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 1500)")
time.sleep(2)

#Click Additional episodes
AdditonalEp1 = driver.find_element(By.ID, 'undefined-1').click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 1500)")
time.sleep(2)

AdditonalEp2 = driver.find_element(By.ID, 'undefined-2').click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 1700)")
time.sleep(2)
#More like this carousel shows