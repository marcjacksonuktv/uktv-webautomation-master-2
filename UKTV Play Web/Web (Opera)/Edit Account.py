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

# Header
uktvplaylogo = driver.find_element(By.ID, 'nav-bar-home')
categories = driver.find_element(By.ID, 'nav-bar-categories')
channels = driver.find_element(By.ID, 'nav-bar-channels')
boxsets = driver.find_element(By.ID, 'nav-bar-boxsets')
a2z = driver.find_element(By.ID, 'nav-bar-az')
more = driver.find_element(By.ID, 'nav-bar-more')
mylist = driver.find_element(By.ID, 'nav-bar-mylist')
account = driver.find_element(By.ID, 'nav-bar-account')
search = driver.find_element(By.ID, 'nav-bar-search')

# Sign In
account.click()
email = driver.find_element(By.ID, 'email').send_keys('operauser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('password123')
SignIn_button = driver.find_element(By.ID, 'sign-in-btn').click()
time.sleep(3)

# My Account
accountpage = driver.find_element(By.ID, 'nav-bar-account').click()
time.sleep(3)
emailedit = driver.find_element(By.ID, 'email-edit')
emailedit.click()
emaileditcancel = driver.find_element(By.ID, 'email-cancel').click()
emailedit.click()
driver.implicitly_wait(10)
emailtext = driver.find_element(By.ID, 'email').send_keys('operauseredit@testaccount.com')
saveedit = driver.find_element(By.ID, 'email-save').click()
time.sleep(1)

# First Name
firstnameedit = driver.find_element(By.ID, 'first-name-edit')
firstnameedit.click()
firstnameeditcancel = driver.find_element(By.ID, 'first-name-cancel').click()
firstnameedit.click()
driver.implicitly_wait(10)
firstnametext = driver.find_element(By.ID, 'first-name').send_keys('Gene')
saveedit = driver.find_element(By.ID, 'first-name-save').click()
time.sleep(1)

# Last Name
lastnameedit = driver.find_element(By.ID, 'last-name-edit')
lastnameedit.click()
lastnameeditcancel = driver.find_element(By.ID, 'last-name-cancel').click()
lastnameedit.click()
driver.implicitly_wait(10)
lastnametext = driver.find_element(By.ID, 'last-name').send_keys('Eric')
saveedit = driver.find_element(By.ID, 'last-name-save').click()
time.sleep(1)

# Gender
genderedit = driver.find_element(By.ID, 'gender-edit')
genderedit.click()
gendereditcancel = driver.find_element(By.ID, 'gender-cancel').click()
genderedit.click()
driver.implicitly_wait(10)
genderdropdown = driver.find_element(By.ID, 'gender').click()
otherdd = driver.find_element(By.ID, 'gender-NotKnown')
femaledd = driver.find_element(By.ID, 'gender-Female')
maledd = driver.find_element(By.ID, 'gender-Male').click()
saveedit = driver.find_element(By.ID, 'gender-save').click()
time.sleep(1)

# Date of Birth
dobedit = driver.find_element(By.ID, 'date-edit')
dobedit.click()
dobeditcancel = driver.find_element(By.ID, 'date-cancel').click()
dobedit.click()
driver.implicitly_wait(10)
day = driver.find_element(By.ID, '_DateOfBirth_Day')
month = driver.find_element(By.ID, '_DateOfBirth_Month')
year = driver.find_element(By.ID, '_DateOfBirth_Year')
day.click()
dayedit = driver.find_element(By.ID, 'day-13').click()
month.click()
monthedit = driver.find_element(By.ID, 'month-10').click()
year.click()
yearedit = driver.find_element(By.ID, 'year-1985').click()
saveedit = driver.find_element(By.ID, 'date-save').click()
time.sleep(1)

# Postcode
postcodeedit = driver.find_element(By.ID, 'postcode-edit')
postcodeedit.click()
postcodeeditcancel = driver.find_element(By.ID, 'postcode-cancel').click()
postcodeedit.click()
driver.implicitly_wait(10)
postcodetext = driver.find_element(By.ID, 'postcode').send_keys('HA9 0WS')
saveedit = driver.find_element(By.ID, 'postcode-save').click()
time.sleep(1)

# Password
changepwdd = driver.find_element(By.ID, 'password-tab').click()
passwordedit = driver.find_element(By.ID, 'password-edit').click()
passwordcancel = driver.find_element(By.ID, 'password-cancel').click()
passwordedit2 = driver.find_element(By.ID, 'password-edit').click()
currentpassword = driver.find_element(By.ID, 'currentPassword').send_keys('password123')
newpassword = driver.find_element(By.ID, 'newPassword').send_keys('password1')
saveedit = driver.find_element(By.ID, 'password-save').click()
time.sleep(1)

# Preferences
prefdd = driver.find_element(By.ID, 'preferences-tab').click()
prefedit = driver.find_element(By.ID, 'targetedAdsOptOut').click()
time.sleep(2)

# Communication
comdd = driver.find_element(By.ID, 'communication-tab').click()
comedit = driver.find_element(By.ID, 'newsletter-edit').click()
comcancel = driver.find_element(By.ID, 'newsletter-cancel').click()
comedi2 = driver.find_element(By.ID, 'newsletter-edit').click()
subscribe = driver.find_element(By.ID, 'subscribeNewsletter').click()
time.sleep(1)

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