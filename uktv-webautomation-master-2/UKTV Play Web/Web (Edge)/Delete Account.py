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
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
testurl = 'https://uktvplay.uktv.co.uk/'
a = ActionChains(driver)
driver.get(testurl)
driver.implicitly_wait(15)

# Cookie Notice
CookieYes = driver.find_element_by_id('cookie-agree').click()
time.sleep(2)

#My Account
MyAccount = driver.find_element_by_id('nav-bar-account')
MyAccount.click()
time.sleep(2)

#Sign In
email = driver.find_element_by_id('email').send_keys('edgeuser@testaccount.com')
password = driver.find_element_by_id('password').send_keys('password123')
SignIn_button = driver.find_element_by_id('sign-in-btn').click()
time.sleep(2)

#My Account
MyAccount = driver.find_element_by_id('nav-bar-account')
MyAccount.click()
time.sleep(8)

# driver.execute_script("window.scrollTo(0, 2000)")

# Close Account
CloseAccount = driver.find_element_by_id('close-tab')
CloseAccount.click()
time.sleep(2)
Delete = driver.find_element_by_id('delete')
Delete.click()
time.sleep(2)
DeleteButton = driver.find_element_by_id('delete-account-button')
DeleteButton.click()
time.sleep(2)