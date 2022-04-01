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
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
testurl = 'https://uktv:wemakegreattv@uktvplay.uatuktv.co.uk/'
a = ActionChains(driver)
driver.set_window_size(500, 1000)
driver.get(testurl)
driver.implicitly_wait(10)

# Cookie Notice
CookieYes = driver.find_element_by_id('cookie-agree').click()
time.sleep(2)

# Burger Menu
BurgerMenu = driver.find_element_by_id('mobile-nav-menu').click()
time.sleep(2)

# My Account Register
MyAccount = driver.find_element_by_id('side-nav-account')
MyAccount.click()
time.sleep(2)

#Sign In
email = driver.find_element_by_id('email').send_keys('chromeusermob@testaccount.com')
password = driver.find_element_by_id('password').send_keys('password123')
SignIn_button = driver.find_element_by_id('sign-in-btn').click()
time.sleep(2)

# Burger Menu
BurgerMenu = driver.find_element_by_id('mobile-nav-menu').click()
time.sleep(2)

# My Account Register
MyAccount = driver.find_element_by_id('side-nav-account')
MyAccount.click()
time.sleep(8)

# driver.execute_script("window.scrollTo(0, 2000)")

#Click Close Account
CloseAccount = driver.find_element_by_id('close-tab')
CloseAccount.click()
time.sleep(2)

#Click Delete
Delete = driver.find_element_by_id('delete')
Delete.click()
time.sleep(2)

#Click Delete Account
DeleteButton = driver.find_element_by_id('delete-account-button')
DeleteButton.click()
time.sleep(2)