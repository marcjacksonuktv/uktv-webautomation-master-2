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
options = Options()
from selenium import webdriver
driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
testurl = 'https://uktvplay.uktv.co.uk/'
a = ActionChains(driver)
driver.get(testurl)
driver.implicitly_wait(15)

# Cookie Notice
CookieYes = driver.find_element_by_id('cookie-agree').click()
time.sleep(2)

# My Account
MyAccount = driver.find_element_by_id('nav-bar-account')
MyAccount.click()
time.sleep(2)

# Sign In
email = driver.find_element_by_id('email').send_keys('safariuser@testaccount.com')
password = driver.find_element_by_id('password').send_keys('password123')
SignIn_button = driver.find_element_by_id('sign-in-btn').click()
time.sleep(3)

# Sign Out
accountsignedin = driver.find_element_by_id('nav-bar-account')
accountsignedin.click()
signout = driver.find_element_by_id('sign-out')
time.sleep(10)
signout.click()

print('Sign In & Sign Out Passed')
