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

# My Account Register
MyAccount = driver.find_element(By.ID,'side-nav-account')
MyAccount.click()
time.sleep(2)
RegistertoWatch = driver.find_element(By.ID,'register-to-watch-btn')
RegistertoWatch.click()
time.sleep(2)

# Register Form
email = driver.find_element(By.ID,'email').send_keys('chromeusermob@testaccount.com')
password = driver.find_element(By.ID,'password').send_keys('Passw0rd123!')

FirstName = driver.find_element(By.ID,'firstName').send_keys('Gurjeet')
LastName = driver.find_element(By.ID,'lastName').send_keys('Kaur')

day = driver.find_element(By.ID,'dateOfBirthDay')
month = driver.find_element(By.ID,'dateOfBirthMonth')
year = driver.find_element(By.ID,'dateOfBirthYear')
day.click()
dayedit = driver.find_element(By.XPATH,'//*[@id="dateOfBirthDay"]/option[12]').click()
month.click()
monthedit = driver.find_element(By.XPATH,'//*[@id="dateOfBirthMonth"]/option[6]').click()
year.click()
yearedit = driver.find_element(By.XPATH,'//*[@id="dateOfBirthYear"]/option[38]').click()

Gender = driver.find_element(By.ID,'gender').send_keys('Female')
Postcode = driver.find_element(By.ID,'postCode').send_keys('W6 7AP')

News_opt_in = driver.find_element(By.ID,'subscribeNewsletter').click()

Registertowatch_button = driver.find_element(By.ID,'register-btn').click()
time.sleep(5)
