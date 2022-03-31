import sys
import time
from time import gmtime, strftime
import datetime
import conf as conf
import self as self
now = datetime.datetime.now()
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
from webdriver_manager.opera import OperaDriverManager
driver = webdriver.Opera(executable_path=OperaDriverManager().install())
testurl = 'https://uktv:wemakegreattv@uktvplay.ppdevuktv.co.uk/'
a = ActionChains(driver)
driver.set_window_size(500, 1000)
driver.get(testurl)
driver.implicitly_wait(10)

# Cookie Notice
CookieYes = driver.find_element(By.ID,'cookie-agree').click()
time.sleep(2)

# Burger Menu
BurgerMenu = driver.find_element(By.ID, 'mobile-nav-menu').click()
time.sleep(2)

# My Sign In
MyAccount_SignIn = driver.find_element(By.ID, 'side-nav-signin')
MyAccount_SignIn.click()
time.sleep(2)

# Sign In
email = driver.find_element(By.ID,'email').send_keys('chromeusermob@testaccount.com')
password = driver.find_element(By.ID,'password').send_keys('Passw0rd123!')
SignIn_button = driver.find_element(By.ID,'sign-in-btn').click()
time.sleep(3)

# Burger Menu
BurgerMenu = driver.find_element(By.ID,'mobile-nav-menu').click()
time.sleep(2)

# My Account
accountpage = driver.find_element(By.ID,'side-nav-account').click()
time.sleep(3)
emailedit = driver.find_element(By.ID,'profile-edit-email')
emailedit.click()
emaileditcancel = driver.find_element(By.ID,'email-cancel').click()
emailedit.click()
driver.implicitly_wait(10)
emailtext = driver.find_element(By.ID,'email').send_keys('chromeuseredit@testaccount.com')
saveedit = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[1]/div[2]/span[2]/input').click()
time.sleep(3)

# First Name
firstnameedit = driver.find_element(By.ID,'profile-edit-firstname')
firstnameedit.click()
firstnameeditcancel = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[2]/div[2]/span[2]/a').click()
firstnameedit.click()
driver.implicitly_wait(10)
firstnametext = driver.find_element(By.ID,'firstName').send_keys('Gene')
saveedit = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[2]/div[2]/span[2]/input').click()
time.sleep(3)

# Last Name
lastnameedit = driver.find_element(By.ID,'profile-edit-lastname')
lastnameedit.click()
driver.implicitly_wait(10)
lastnameeditcancel = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[3]/div[2]/span[2]/a').click()
lastnameedit.click()
driver.implicitly_wait(10)
lastnametext = driver.find_element(By.ID,'lastName').send_keys('Eric')
saveedit = driver.find_element(By.XPATH, '//*[@id="profileForm"]/div[3]/div[2]/span[2]/input').click()
time.sleep(3)

# Gender
genderedit = driver.find_element(By.ID,'profile-edit-gender')
genderedit.click()
gendereditcancel = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[4]/div[2]/span[2]/a').click()
genderedit.click()
driver.implicitly_wait(10)
genderdropdown = driver.find_element(By.ID, 'gender').click()
otherdd = driver.find_element(By.XPATH,'//*[@id="gender"]/option[4]')
femaledd = driver.find_element(By.XPATH,'//*[@id="gender"]/option[3]')
maledd = driver.find_element(By.XPATH,'//*[@id="gender"]/option[2]').click()
saveedit = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[4]/div[2]/span[2]/input').click()
time.sleep(3)

# Date of Birth
dobedit = driver.find_element(By.ID,'profile-edit-dob')
dobedit.click()
dobeditcancel = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[5]/div[2]/span[2]/a').click()
dobedit.click()
driver.implicitly_wait(10)
day = driver.find_element(By.ID,'dateOfBirthDay')
month = driver.find_element(By.ID,'dateOfBirthMonth')
year = driver.find_element(By.ID,'dateOfBirthYear')
day.click()
dayedit = driver.find_element(By.XPATH,'//*[@id="dateOfBirthDay"]/option[14]').click()
month.click()
monthedit = driver.find_element(By.XPATH,'//*[@id="dateOfBirthMonth"]/option[8]').click()
year.click()
yearedit = driver.find_element(By.XPATH,'//*[@id="dateOfBirthYear"]/option[43]').click()
saveedit = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[5]/div[2]/span[2]/input').click()
time.sleep(3)

# Postcode
postcodeedit = driver.find_element(By.ID,'profile-edit-postcode')
postcodeedit.click()
postcodeeditcancel = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[6]/div[2]/span[2]/a').click()
postcodeedit.click()
driver.implicitly_wait(10)
postcodetext = driver.find_element(By.ID,'postCode').send_keys('HA9 0WS')
saveedit = driver.find_element(By.XPATH,'//*[@id="profileForm"]/div[6]/div[2]/span[2]/input').click()
time.sleep(1)
accountpage = driver.find_element(By.ID,'password-tab').click()
time.sleep(3)

# Password
passwordedit = driver.find_element(By.ID,'profile-edit-password').click()
passwordcancel = driver.find_element(By.XPATH,'//*[@id="password-tab"]/div/div[2]/span/a').click()
passwordedit2 = driver.find_element(By.XPATH,'//*[@id="profile-edit-password"]').click()
currentpassword = driver.find_element(By.ID,'password').send_keys('Passw0rd123!')
newpassword = driver.find_element(By.ID,'newPassword').send_keys('Passw0rd1234!')
saveedit = driver.find_element(By.XPATH,'//*[@id="password-tab"]/div/div[2]/span/input').click()
time.sleep(3)

# Preferences
prefdd = driver.find_element(By.ID,'preferences-tab').click()
prefedit = driver.find_element(By.ID,'targetedAdsOptOut').click()
time.sleep(2)

# Communication
comdd = driver.find_element(By.ID,'communication-tab').click()
comedit = driver.find_element(By.ID,'newsletter-edit').click()
comcancel = driver.find_element(By.ID,'newsletter-cancel').click()
comedi2 = driver.find_element(By.ID,'newsletter-edit').click()
subscribe = driver.find_element(By.ID,'subscribeNewsletter').click()
time.sleep(1)

# Close Account
CloseAccount = driver.find_element(By.ID,'close-tab')
CloseAccount.click()
time.sleep(2)
Delete = driver.find_element(By.ID,'delete')
Delete.click()
time.sleep(2)
DeleteButton = driver.find_element(By.ID,'delete-account-button')
DeleteButton.click()
time.sleep(2)