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
time.sleep(30)

# My Account Register
MyAccount = driver.find_element(By.ID, 'nav-bar-account')
MyAccount.click()
time.sleep(30)
RegistertoWatch = driver.find_element(By.ID, 'register-to-watch-btn').click()
time.sleep(25)

# Register Form
email = driver.find_element(By.ID, 'emailAddress').send_keys('safariuser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('Password123!!')

FirstName = driver.find_element(By.ID, 'firstName').send_keys('Test')
LastName = driver.find_element(By.ID, 'lastName').send_keys('Analyst')

DoB_Day = driver.find_element(By.ID, 'dateOfBirthDay').send_keys('1')
DoB_Month = driver.find_element(By.ID, 'dateOfBirthMonth').send_keys('1')
DoB_Year = driver.find_element(By.ID, 'dateOfBirthYear').send_keys('1995')

Gender = driver.find_element(By.ID, 'gender').send_keys('Other')
Postcode = driver.find_element(By.ID, 'postCode').send_keys('W6 7AP')

News_opt_in = driver.find_element(By.ID, 'subscribeNewsletter').click()

Registertowatch_button = driver.find_element(By.ID, 'register-btn').click()
time.sleep(5)
RegisterationComplete_Continuebutton = driver.find_element(By.ID,'account-continue').click()

print('Registration Complete')
