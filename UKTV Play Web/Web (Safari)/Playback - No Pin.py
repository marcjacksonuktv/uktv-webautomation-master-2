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

# Sign In
account.click()
email = driver.find_element(By.ID, 'email').send_keys('safariuser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('Password123!!')
SignIn_button = driver.find_element(By.ID, 'sign-in-btn').click()
time.sleep(3)

#Search
search5 = driver.find_element(By.ID, 'nav-bar-search').click()
SearchBar = driver.find_element(By.CLASS_NAME,'search-input').send_keys('dave gorman')
time.sleep(1)
ClickResult = driver.find_element(By.XPATH,'//*[@id="search-result-2"]/div/p[1]')
ClickResult.click()

#Continue without Pin
ContinueWithoutPin = driver.find_element(By.ID, 'continue-pin')
ContinueWithoutPin.click()

#Add to Favourites
Add = driver.find_element(By.ID, 'add-to-favourites')
Add.click()

#Click on My List
MyList = driver.find_element(By.ID, 'nav-bar-mylist')
MyList.click()
driver.execute_script("window.history.go(-1)")

#Click to share
#Share = driver.find_element(By.ID, 'Share-Icon')
#Share.click()
#driver.execute_script("window.scrollTo(0, 700)")

#Click on Facebook
#FacebookShare = driver.find_element(By.ID, 'facebook-share')
#FacebookShare.click()
#driver.switch_to.window(driver.window_handles[0])

#Click on Twitter
#TwitterShare = driver.find_element(By.ID, 'twitter-share')
#TwitterShare.click()
#driver.switch_to.window(driver.window_handles[0])
#time.sleep(2)

#Continue without Pin
ContinueWithoutPin = driver.find_element(By.ID, 'continue-pin')
ContinueWithoutPin.click()

#Click to Autoplay
AutoplayOffOn = driver.find_element(By.ID, 'Layer_1')
a.send_keys_to_element(AutoplayOffOn, Keys.ENTER * 3).perform()

#Start Playback
PlayButton = driver.find_element(By.XPATH, '//*[@id="restart-link"]/div/div[2]')
PlayButton.click()
time.sleep(180)

print('Playback - No Pin Passed')