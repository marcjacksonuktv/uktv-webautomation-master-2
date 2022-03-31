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
driver.get('https://uktvplay.uktv.co.uk/shows/meet-the-richardsons/watch-online')
time.sleep(2)

#Enable Pin
EnablePin = driver.find_element(By.ID, 'enable-pin')
EnablePin.click()
Over15Button = driver.find_element(By.ID, 'over-15')
Over15Button.click()
Pin1 = driver.find_element(By.ID, 'input-0').send_keys('1')
Pin2 = driver.find_element(By.ID, 'input-1').send_keys('1')
Pin3 = driver.find_element(By.ID, 'input-2').send_keys('1')
Pin4 = driver.find_element(By.ID, 'input-3').send_keys('1')
time.sleep(2)
EnablePin = driver.find_element(By.ID, 'enable-pin')
EnablePin.click()
UnlockPin = driver.find_element(By.ID, 'unlock-pin')
UnlockPin.click()

#Add to Favourites
Add = driver.find_element(By.ID, 'add-to-favourites')
Add.click()

#Click on My List
MyList = driver.find_element(By.ID, 'nav-bar-mylist')
MyList.click()
driver.execute_script("window.history.go(-1)")

#Click to share
#Share = driver.find_element(By.XPATH, '//*[@id="episode-details"]/div/div[3]/div[1]/button')
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

#Enter Pin
Pin1 = driver.find_element(By.ID, 'input-0').send_keys('1')
Pin2 = driver.find_element(By.ID, 'input-1').send_keys('1')
Pin3 = driver.find_element(By.ID, 'input-2').send_keys('1')
Pin4 = driver.find_element(By.ID, 'input-3').send_keys('1')
time.sleep(2)
UnlockPin = driver.find_element(By.ID, 'unlock-pin')
UnlockPin.click()

#Click to Autoplay
AutoplayOffOn = driver.find_element(By.ID, 'Layer_1')
a.send_keys_to_element(AutoplayOffOn, Keys.ENTER * 3).perform()

#Start Playback
PlayButton = driver.find_element(By.ID, 'start-playback')
PlayButton.click()
time.sleep(120)

print('Playback - Pin Enabled Passed')