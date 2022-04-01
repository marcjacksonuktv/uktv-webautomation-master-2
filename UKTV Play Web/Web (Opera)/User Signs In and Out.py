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
time.sleep(2)

# My Account
MyAccount = driver.find_element(By.ID, 'nav-bar-account')
MyAccount.click()
time.sleep(2)

# Sign In
email = driver.find_element(By.ID, 'email').send_keys('operauser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('password123')
SignIn_button = driver.find_element(By.ID, 'sign-in-btn').click()
time.sleep(3)

# Sign Out
accountsignedin = driver.find_element(By.ID, 'nav-bar-account')
accountsignedin.click()
signout = driver.find_element(By.ID, 'sign-out')
time.sleep(10)
signout.click()

print('Sign In & Sign Out Passed')
