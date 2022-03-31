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

# Header
uktvplaylogo = driver.find_element_by_id('nav-bar-home')
categories = driver.find_element_by_id('nav-bar-categories')
channels = driver.find_element_by_id('nav-bar-channels')
boxsets = driver.find_element_by_id('nav-bar-boxsets')
a2z = driver.find_element_by_id('nav-bar-az')
more = driver.find_element_by_id('nav-bar-more')
mylist = driver.find_element_by_id('nav-bar-mylist')
account = driver.find_element_by_id('nav-bar-account')
search = driver.find_element_by_id('nav-bar-search')

# Sign In
account.click()
email = driver.find_element_by_id('email').send_keys('edgeuser@testaccount.com')
password = driver.find_element_by_id('password').send_keys('password123')
SignIn_button = driver.find_element_by_id('sign-in-btn').click()
time.sleep(3)

# My Account
accountpage = driver.find_element_by_id('nav-bar-account').click()
time.sleep(3)
emailedit = driver.find_element_by_id('email-edit')
emailedit.click()
emaileditcancel = driver.find_element_by_id('email-cancel').click()
emailedit.click()
driver.implicitly_wait(10)
emailtext = driver.find_element_by_id('email').send_keys('edgeuseredit@testaccount.com')
saveedit = driver.find_element_by_id('email-save').click()
time.sleep(1)

# First Name
firstnameedit = driver.find_element_by_id('first-name-edit')
firstnameedit.click()
firstnameeditcancel = driver.find_element_by_id('first-name-cancel').click()
firstnameedit.click()
driver.implicitly_wait(10)
firstnametext = driver.find_element_by_id('first-name').send_keys('Gene')
saveedit = driver.find_element_by_id('first-name-save').click()
time.sleep(1)

# Last Name
lastnameedit = driver.find_element_by_id('last-name-edit')
lastnameedit.click()
lastnameeditcancel = driver.find_element_by_id('last-name-cancel').click()
lastnameedit.click()
driver.implicitly_wait(10)
lastnametext = driver.find_element_by_id('last-name').send_keys('Eric')
saveedit = driver.find_element_by_id('last-name-save').click()
time.sleep(1)

# Gender
genderedit = driver.find_element_by_id('gender-edit')
genderedit.click()
gendereditcancel = driver.find_element_by_id('gender-cancel').click()
genderedit.click()
driver.implicitly_wait(10)
genderdropdown = driver.find_element_by_id('gender').click()
otherdd = driver.find_element_by_id('gender-NotKnown')
femaledd = driver.find_element_by_id('gender-Female')
maledd = driver.find_element_by_id('gender-Male').click()
saveedit = driver.find_element_by_id('gender-save').click()
time.sleep(1)

# Date of Birth
dobedit = driver.find_element_by_id('date-edit')
dobedit.click()
dobeditcancel = driver.find_element_by_id('date-cancel').click()
dobedit.click()
driver.implicitly_wait(10)
day = driver.find_element_by_id('_DateOfBirth_Day')
month = driver.find_element_by_id('_DateOfBirth_Month')
year = driver.find_element_by_id('_DateOfBirth_Year')
day.click()
dayedit = driver.find_element_by_id('day-13').click()
month.click()
monthedit = driver.find_element_by_id('month-10').click()
year.click()
yearedit = driver.find_element_by_id('year-1985').click()
saveedit = driver.find_element_by_id('date-save').click()
time.sleep(1)

# Postcode
postcodeedit = driver.find_element_by_id('postcode-edit')
postcodeedit.click()
postcodeeditcancel = driver.find_element_by_id('postcode-cancel').click()
postcodeedit.click()
driver.implicitly_wait(10)
postcodetext = driver.find_element_by_id('postcode').send_keys('HA9 0WS')
saveedit = driver.find_element_by_id('postcode-save').click()
time.sleep(1)

# Password
changepwdd = driver.find_element_by_id('password-tab').click()
passwordedit = driver.find_element_by_id('password-edit').click()
passwordcancel = driver.find_element_by_id('password-cancel').click()
passwordedit2 = driver.find_element_by_id('password-edit').click()
currentpassword = driver.find_element_by_id('currentPassword').send_keys('password123')
newpassword = driver.find_element_by_id('newPassword').send_keys('password1')
saveedit = driver.find_element_by_id('password-save').click()
time.sleep(1)

# Preferences
prefdd = driver.find_element_by_id('preferences-tab').click()
prefedit = driver.find_element_by_id('targetedAdsOptOut').click()
time.sleep(2)

# Communication
comdd = driver.find_element_by_id('communication-tab').click()
comedit = driver.find_element_by_id('newsletter-edit').click()
comcancel = driver.find_element_by_id('newsletter-cancel').click()
comedi2 = driver.find_element_by_id('newsletter-edit').click()
subscribe = driver.find_element_by_id('subscribeNewsletter').click()
time.sleep(1)