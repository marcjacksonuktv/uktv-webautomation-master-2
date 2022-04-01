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

testurl = 'https://uktv:wemakegreattv@uktvplay.ppuktv.co.uk/'
a = ActionChains(driver)
driver.get(testurl)
driver.implicitly_wait(10)

# Cookie Notice
CookieYes = driver.find_element(By.ID, 'cookie-agree').click()
time.sleep(2)

#My Account
MyAccount = driver.find_element(By.ID, 'nav-bar-account')
MyAccount.click()
time.sleep(2)

#Sign In
email = driver.find_element(By.ID, 'email').send_keys('chromeuser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('Password123!!')
SignIn_button = driver.find_element(By.ID, 'sign-in-btn').click()
time.sleep(2)

#My Account
MyAccount = driver.find_element(By.ID, 'nav-bar-account')
MyAccount.click()
time.sleep(8)

# driver.execute_script("window.scrollTo(0, 2000)")

# Close Account
CloseAccount = driver.find_element(By.ID, 'close-tab')
CloseAccount.click()
time.sleep(2)
Delete = driver.find_element(By.ID, 'delete')
Delete.click()
time.sleep(2)
DeleteButton = driver.find_element(By.ID, 'delete-account-button')
DeleteButton.click()
time.sleep(2)