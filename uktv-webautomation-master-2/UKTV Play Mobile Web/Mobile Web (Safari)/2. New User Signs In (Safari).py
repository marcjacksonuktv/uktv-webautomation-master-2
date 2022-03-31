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
testurl = 'https://uktv:wemakegreattv@uktvplay.ppdevuktv.co.uk/'
driver.set_window_size(500, 1000)
a = ActionChains(driver)
driver.get(testurl)
driver.implicitly_wait(10)

# Cookie Notice
CookieYes = driver.find_element(By.ID,'cookie-agree').click()
time.sleep(2)

# Burger Menu
BurgerMenu = driver.find_element(By.ID,'mobile-nav-menu').click()
time.sleep(2)

# My Sign In
MyAccount_SignIn = driver.find_element(By.ID,'side-nav-signin')
MyAccount_SignIn.click()
time.sleep(2)

# Sign In
email = driver.find_element(By.ID,'email').send_keys('chromeusermob@testaccount.com')
password = driver.find_element(By.ID,'password').send_keys('Passw0rd123!')
SignIn_button = driver.find_element(By.ID,'sign-in-btn').click()
time.sleep(6)