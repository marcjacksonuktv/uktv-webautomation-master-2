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
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
testurl = 'https://uktv:wemakegreattv@uktvplay.ppevuktv.co.uk/'
a = ActionChains(driver)
driver.set_window_size(500, 1000)
driver.get(testurl)
driver.implicitly_wait(10)

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