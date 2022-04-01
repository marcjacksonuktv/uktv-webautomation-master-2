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
time.sleep(2)

# My Account Register
MyAccount = driver.find_element(By.ID, 'nav-bar-account')
MyAccount.click()
time.sleep(2)
RegistertoWatch = driver.find_element(By.ID, 'register-now-link')
RegistertoWatch.click()
time.sleep(2)

# Register Form
email = driver.find_element(By.ID, 'emailAddress').send_keys('safariuser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('Password123!!')

FirstName = driver.find_element(By.ID, 'firstName').send_keys('Test')
LastName = driver.find_element(By.ID, 'lastName').send_keys('Analyst')

DateofBirt_Day = driver.find_element(By.ID, 'registration_DateOfBirth_Day').send_keys('1')
DateofBirt_Month = driver.find_element(By.ID, 'registration_DateOfBirth_Month').send_keys('1')
DateofBirt_Year = driver.find_element(By.ID, 'registration_DateOfBirth_Year').send_keys('1995')

Gender = driver.find_element(By.ID, 'gender').send_keys('Other')
Postcode = driver.find_element(By.ID, 'postCode').send_keys('W6 7AP')

News_opt_in = driver.find_element(By.ID, 'subscribeNewsletter').click()

Registertowatch_button = driver.find_element(By.ID, 'register-btn').click()
time.sleep(5)
RegisterationComplete_Continuebutton = driver.find_element_(By.CLASS_NAME,'submit-button').click()

print('Registration Complete')
