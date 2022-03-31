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

# My Account Register
MyAccount = driver.find_element(By.ID, 'nav-bar-account')
MyAccount.click()
time.sleep(2)
RegistertoWatch = driver.find_element(By.ID, 'register-to-watch-btn')
RegistertoWatch.click()
time.sleep(2)

# Register Form
email = driver.find_element(By.ID, 'email').send_keys('chromeuser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('Password123!!')

FirstName = driver.find_element(By.ID, 'firstName').send_keys('Test')
LastName = driver.find_element(By.ID, 'lastName').send_keys('Analyst')

DoB_Day = driver.find_element(By.ID, 'dateOfBirthDay').send_keys('1')
DoB_Month = driver.find_element(By.ID, 'dateOfBirthMonth').send_keys('1')
DoB_Year = driver.find_element(By.ID, 'dateOfBirthYear').send_keys('1995')

Gender = driver.find_element(By.ID, 'gender').send_keys('Other')
Postcode = driver.find_element(By.ID, 'postCode').send_keys('W6 7AP')

News_opt_in = driver.find_element(By.ID, 'subscribeNewsletter').click()

# Add in Privacy Policy, T&C, Cookies Policy & alt Sign In Checks

Registertowatch_button = driver.find_element(By.ID, 'register-btn').click()
time.sleep(5)
RegisterationComplete_Continuebutton = driver.find_element(By.ID,'account-continue').click()

print('Registration Complete')
