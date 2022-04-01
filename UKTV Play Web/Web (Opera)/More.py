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
testurl = 'https://www.uktvplay.ppuktv.co.uk/'
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

# More
more = driver.find_element(By.ID, 'nav-bar-more').click()

# What is UKTV Play
whatistab = driver.find_element(By.ID, 'tab-what-is-uktv-play')
davelink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[1]/a[1]')
print(davelink.get_attribute('href'))
dramalink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[1]/a[2]')
print(dramalink.get_attribute('href'))
yesterdaylink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[1]/a[3]')
print(yesterdaylink.get_attribute('href'))
waystowatchlink1 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[2]/a')
print(waystowatchlink1.get_attribute('href'))
mylistlink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/ul/li[4]/a')
print(mylistlink.get_attribute('href'))
waystowatchlink2 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[6]/a')
print(waystowatchlink2.get_attribute('href'))
contactuslink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[9]/a')
print(contactuslink.get_attribute('href'))

# Ways to Watch
driver.get('https://uktvplay.uktv.co.uk/ways-to-watch')
CookieYes = driver.find_element(By.ID, 'cookie-agree').click()
time.sleep(1)
driver.get('https://uktvplay.uktv.co.uk/ways-to-watch/web')
time.sleep(1)
driver.get('https://uktvplay.uktv.co.uk/ways-to-watch/mobile')
time.sleep(1)
driver.get('https://uktvplay.uktv.co.uk/ways-to-watch/tv')
time.sleep(1)
driver.get('https://uktvplay.uktv.co.uk/ways-to-watch/streaming')
time.sleep(1)

# Set PIN
driver.get('https://uktvplay.uktv.co.uk/parental-controls')
time.sleep(5)
fifteenplus = driver.find_element(By.ID, 'over-15').click()
input1 = driver.find_element(By.ID, 'input-0').send_keys('1')
input2 = driver.find_element(By.ID, 'input-1').send_keys('2')
input3 = driver.find_element(By.ID, 'input-2').send_keys('3')
input4 = driver.find_element(By.ID, 'input-3').send_keys('4')
time.sleep(1)
EnablePin = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section[2]/div/button').click()
time.sleep(1)
# Remove Pin
RemovePin = driver.find_element(By.XPATH,  '/html/body/div/div/div/div/main/div/section/div/div/button').click()
input1 = driver.find_element(By.ID, 'input-0').send_keys('1')
input2 = driver.find_element(By.ID, 'input-1').send_keys('2')
input3 = driver.find_element(By.ID, 'input-2').send_keys('3')
input4 = driver.find_element(By.ID, 'input-3').send_keys('4')
RemovePin2 = driver.find_element(By.XPATH,  '/html/body/div/div/div/div/main/div/section/div/div/button').click()

# Accessibility
driver.get('https://uktvplay.uktv.co.uk/accessibility')
time.sleep(1)
a2zhref = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/div/p[3]/a')
print(a2zhref.get_attribute('href'))
contacthref = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[7]/a')
print(contacthref.get_attribute('href'))

# Help
driver.get('https://uktvplay.uktv.co.uk/help/faqs')
time.sleep(1)

# faqs
davelink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[1]/a[1]')
print(davelink.get_attribute('href'))
dramalink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[1]/a[2]')
print(dramalink.get_attribute('href'))
yesterdaylink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[1]/a[3]')
print(yesterdaylink.get_attribute('href'))
wtwlink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[2]/a')
print(wtwlink.get_attribute('href'))
streaminglink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[3]/a')
print(streaminglink.get_attribute('href'))
deviceslink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[4]/a')
print(deviceslink.get_attribute('href'))
twitterlink1 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[5]/a')
print(twitterlink1.get_attribute('href'))
twitterlink2 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[6]/a[1]')
print(twitterlink2.get_attribute('href'))
helpdesklink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[6]/a[2]')
print(helpdesklink.get_attribute('href'))
twitterlink3 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[19]/a[1]')
print(twitterlink3.get_attribute('href'))
helpdesklink2 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[19]/a[2]')
print(helpdesklink2.get_attribute('href'))
# website
driver.get('https://uktvplay.uktv.co.uk/help/website')
time.sleep(1)
# mobile/tablet
driver.get('https://uktvplay.uktv.co.uk/help/mobile-tablet')
appstorelink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[3]/a')
print(appstorelink.get_attribute('href'))
googleplaylink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[5]/a[1]')
print(googleplaylink.get_attribute('href'))
amazonstorelink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[5]/a[2]')
print(amazonstorelink.get_attribute('href'))
twitterlink1 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[12]/a[1]')
print(twitterlink1.get_attribute('href'))
helpdesklink1 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[12]/a[2]')
print(helpdesklink1.get_attribute('href'))
twitterlink2 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[13]/a[1]')
print(twitterlink2.get_attribute('href'))
helpdesklink2 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[13]/a[2]')
print(helpdesklink2.get_attribute('href'))

# tv
driver.get('https://uktvplay.uktv.co.uk/help/tv')
time.sleep(1)
accountlink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/ul/li[3]/a')
print(accountlink.get_attribute('href'))
activatelink = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/ol[1]/li[4]/a')
print(activatelink.get_attribute('href'))
twitterlink2 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[26]/a[1]')
print(twitterlink2.get_attribute('href'))
helpdesklink2 = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section/div/div/p[26]/a[2]')
print(helpdesklink2.get_attribute('href'))

# roku
driver.get('https://uktvplay.uktv.co.uk/help/roku')
time.sleep(1)

# Contact Us
driver.get('https://uktvplay.uktv.co.uk/contact')
time.sleep(1)
twitter = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section[2]/div/div/a[1]')
print(twitter.get_attribute('href'))
facebook = driver.find_element(By.XPATH,  '//*[@id="main-content"]/section[2]/div/div/a[2]')
print(facebook.get_attribute('href'))

print('More Page Passed')